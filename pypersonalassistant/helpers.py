#!/usr/bin/env python3

import sys
import logging

# Log quickstart, using logging stlib
class log(object):
    """
    Easily start logging any python script using the standard `logging`_ library.
    
    .. _logging: https://docs.python.org/3/library/logging.html
    
    :param string logfile: Path to the debug log file. Defaults to <your_script>_py.log
    :param file_level: The `logging level`_ to log to file
    :param stream_level: The `logging level`_ to log to stdout
    :returns: A :py:class:`pypersonalassistant.helpers.log` object
    
    .. _logging level: https://docs.python.org/3.5/library/logging.html#levels
    """
    def __init__(self, logfile=None, file_level=logging.DEBUG, stream_level=logging.WARNING):
        if logfile is None:
            logfile = '{0}.log'.format('_'.join(sys.argv[0].split('.')))
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
        
    def enable(self):
        """
        Enable/re-enable logging
        """
        logging.disable(logging.NOTSET)
        
    def disable(self):
        """
        Disable logging
        """
        logging.disable(logging.CRITICAL)
