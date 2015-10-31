#!/usr/bin/env python3

import sys
import logging

# Log quickstart, using logging stlib
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
