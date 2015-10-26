#!/usr/bin/env python3

import os, sys
import logging
from twilio.rest import TwilioRestClient 

### YOUR CREDENTIALS HERE ###
# python variable name: environment variable name
CREDENTIALS = {
    'TWILIO_ACCOUNT_SID': 'TWILIO_ACCOUNT_SID',
    'TWILIO_AUTH_TOKEN': 'TWILIO_AUTH_TOKEN',
    'PERSONAL_PHONE_NUMBER': 'PERSONAL_PHONE_NUMBER',
    'SMS_GATEWAY_NMUBER': 'TWILIO_PHONE_NUMBER'
    }
for k, v in CREDENTIALS.items():
    try: 
        CREDENTIALS[k] = os.environ[v]
    except KeyError as e:
        CREDENTIALS[k] = None
        logging.warning('Environment variable lookup error with key: {0}'.format(e.args[0]))
#############################

def log_enable(logfile='log.log', file_level=logging.DEBUG, stream_level=logging.WARNING):
    logger = logging.getLogger()
    #logger.setLevel(logging.DEBUG)
    # File log
    fh = logging.FileHandler(logfile)
    fh.setLevel(file_level)
    # Console log
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(stream_level)
    
    # Add format to handlers, add handlers to logger
    handlers = [fh, ch]
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    for h in handlers:
        h.setFormatter(formatter)
        logger.addHandler(h)
    logger.info('~~~ START LOG ~~~')
    return logger
    
def log_disable():
    logging.disable(logging.CRITICAL)
    return None

def twilio_sms(from_, to, body):
    logging.debug('Texting from Twilio')
    logging.info('Twilio credentials to be used:\nAccount SID: {0}\nAuth Token: {1}'.format(CREDENTIALS['TWILIO_ACCOUNT_SID'], str('*'*28)+CREDENTIALS['TWILIO_AUTH_TOKEN'][-4:]))
    logging.info('Twilio SMS to be composed:\nTo: {0}\nFrom: {1}\nBody: {2}'.format(to, from_, body))
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
    return twilio_sms(to, CREDENTIALS['SMS_GATEWAY_NMUBER'], body)

def text_me(body):
    logging.debug('Texting myself')
    return text(CREDENTIALS['PERSONAL_PHONE_NUMBER'], body)
