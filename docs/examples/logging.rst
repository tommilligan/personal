Logging: for easy python debugging
==================================

Start logging
^^^^^^^^^^^^^

The following script allows a user to easily start both logging warnings to stdout and
debug logging to a file, using the standard `logging`_ module.

.. _logging: https://docs.python.org/3/library/logging.html

.. code-block:: python

   import logging
   import pypersonalassistant.helpers

   ppa_logger = pypersonalassistant.helpers.log()
   logging.debug('START LOG')
   
Stop/pause logging
^^^^^^^^^^^^^^^^^^
   
Logging can be easily disabled at any time
   
.. code-block:: python

   ppa_logger.disable()
   ...
   ppa_logger.enable()
   