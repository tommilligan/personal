Logging: for easy python debugging
==================================

Start logging
^^^^^^^^^^^^^

The following script allows a user to easily start logging

* warnings to stdout
* debug to a file

Logging is triggered using the using the standard `logging module`_.
    
.. _logging module: https://docs.python.org/3/library/logging.html

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

Customise logging
^^^^^^^^^^^^^^^^^
   
Details of the underlying logger object can be read or modified to change behaviour,
via the :py:attr:`~pypersonalassistant.helpers.log.logger` attribute
   
.. code-block:: python
    
    ppa_logger.logger.setLevel(logging.INFO)
    

