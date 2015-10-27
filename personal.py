#!/usr/bin/env python3

import argparse
import os
import sys
import logging
import hashlib
import json
import getpass

from Crypto.Cipher import AES
from twilio.rest import TwilioRestClient

CREDENTIALS_PATH = 'credentials.json'

def confirm_input(prompt, method=input):
    value_initial = value_check = None
    while (value_initial != value_check) or (value_initial == None):
            value_initial = method(prompt)
            value_check = method("Confirm: ")
            if value_initial != value_check:
                print('\nPlease try again:')
    return value_initial
    

class AESCipher(object): # http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
    def __init__(self, key): 
        self.bs = 16
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        logging.debug('Raw length {0}'.format(len(raw)))
        raw = self._pad(raw)
        logging.debug('Padded length {0}'.format(len(raw)))
        iv = os.urandom(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return (iv + cipher.encrypt(raw)).hex()

    def decrypt(self, enc):
        enc = enc.encode('utf8')
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).fromhex()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
        
    
class log(object):        
    def __init__(self, logfile='{0}.log'.format('_'.join(sys.argv[0].split('.'))), file_level=logging.DEBUG, stream_level=logging.WARNING):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # File log
        fh = logging.FileHandler(logfile)
        fh.setLevel(file_level)
        # Console log
        ch = logging.StreamHandler()
        ch.setLevel(stream_level)
        # Add format to handlers, add handlers to logger
        handlers = [fh, ch]
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(pathname)s-%(levelname)s-%(message)s')
        for h in handlers:
            h.setFormatter(formatter)
            self.logger.addHandler(h)
        logging.info('~~~ START LOG ~~~')
        
    def enable(self):
        logging.disable(logging.NOTSET)
        
    def disable(self):
        logging.disable(logging.CRITICAL)

#define "personal" calss here, which calls for aes as subobject on init (getpass for UInput)
        
#import getpass
#master_pass = AESCipher(getpass.getpass())

class personal(object):
    def __init__(self): 
        master_pass = confirm_input('Password for personal module: ', method=getpass.getpass)
        master_pass
        
    
def twilio_sms(from_, to, body):
    logging.debug('Texting from Twilio')
    logging.debug('Twilio credentials: {{Account SID: {0}, Auth Token: {1}}}'.format(CREDENTIALS['TWILIO_ACCOUNT_SID'], '*'*32))
    logging.info('Twilio SMS: {{To: {0}, From: {1}, Body: {2}}}'.format(to, from_, body.replace('\n', ' ')))
    client = TwilioRestClient(CREDENTIALS['TWILIO_ACCOUNT_SID'], CREDENTIALS['TWILIO_AUTH_TOKEN']) 
    response = client.messages.create(
        to=to, 
        from_=from_, 
        body=body,  
    )
    logging.debug('Response from Twilio: {0}'.format(response))
    return response

def text(to, body):
    logging.debug('Texting someone')
    return twilio_sms(CREDENTIALS['TWILIO_PHONE_NUMBER'], to, body)

def text_me(body):
    logging.debug('Texting myself')
    return text(CREDENTIALS['PERSONAL_PHONE_NUMBER'], body)

    
    
### YOUR CREDENTIALS - ENVIRONMENT VARIABLES HERE ###
# python variable name: environment variable name

CREDENTIALS = {
    'TWILIO_ACCOUNT_SID': 'TWILIO_ACCOUNT_SID',
    'TWILIO_AUTH_TOKEN': 'TWILIO_AUTH_TOKEN',
    'PERSONAL_PHONE_NUMBER': 'PERSONAL_PHONE_NUMBER',
    'TWILIO_PHONE_NUMBER': 'TWILIO_PHONE_NUMBER',
    'PERSONAL_EMAIL': 'PERSONAL_EMAIL'
    }
for k, v in CREDENTIALS.items():
    try: 
        CREDENTIALS[k] = os.environ[v]
    except KeyError as e:
        CREDENTIALS[k] = None
        #logging.warning('Environment variable lookup error with key: {0}'.format(e.args[0]))
#############################

# Take user input of credentials, store in credentials.json with AES encryption
def main(args):
    
    master_key = confirm_input('Password (hidden): ', method=getpass.getpass)
    master_key_hash = hashlib.sha512(master_key.encode()).digest().hex()
    credentials = {}
    
    # If credentials.json exists, load credentials, check password and exit if not correct
    if os.path.isfile(CREDENTIALS_PATH):
        with open(CREDENTIALS_PATH) as data_file:
            credentials = json.load(data_file)
        if credentials['MASTER_HASH_KEY'] != master_key_hash:
            logging.debug('Password incorrect')
            sys.exit('Password incorrect. Please try again or delete the current credentials.json file')
        logging.debug('Password correct, loading credentials.json')
    # Otherwise, start new credentials file
    else:
        credentials['MASTER_HASH_KEY'] = master_key_hash
        logging.info('Password saved as {0}'.format(master_key_hash))
        print('Password set')
        
    cipher = AESCipher(master_key)
    credentials_required = {
        'TWILIO_ACCOUNT_SID',
        'TWILIO_AUTH_TOKEN',
        'PERSONAL_PHONE_NUMBER',
        'TWILIO_PHONE_NUMBER',
        'PERSONAL_EMAIL',
        'PERSONAL_EMAIL_PASSWORD'
    }
    
    # If --credential is specified, only set that credential
    if args.credential:
        credentials_required = [args.credential]
    
    for cred in credentials_required:
        # If credential is already set, get value. If not (KeyError), carry on execution
        current_encrypted_value = ''
        try:
            current_encrypted_value = credentials[cred]
            # Unless --all flag is raised, only ask for unset credentials
            if (args.all is not True) and (args.credential is False):
                continue
        except KeyError:
            None
        
        prompt = '\nCredential: {0}\nCurrent (encrypted) value: {1}\nEnter new value, or press enter to skip: '.format(cred, current_encrypted_value)
        input_value = confirm_input(prompt)
                
        if input_value == '':
            logging.info('{0} skipped'.format(cred))
            continue
        else:
            encrypted_value = cipher.encrypt(input_value)
            credentials.update({cred: encrypted_value})
            logging.info('{0} updated: {1}'.format(cred, encrypted_value))
    
    with open(CREDENTIALS_PATH, 'w') as outfile:
        json.dump(credentials, outfile)
            

if __name__ == '__main__':
    logger = log()
    parser = argparse.ArgumentParser(description='Editing of credentials.json for personal.py')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--credential', help='update a specific credential')
    group.add_argument('-a', '--all', action='store_true', help='cycle through all credentials')
    args = parser.parse_args()
    main(args)
