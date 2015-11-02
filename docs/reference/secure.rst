.. py:module:: pypersonalassistant.secure
.. py:currentmodule:: pypersonalassistant.secure

:py:mod:`~pypersonalassistant.secure` Module
============================================

The :py:mod:`~pypersonalassistant.secure` module provides a class with the same name which is
used to represent a user's consent to pypersonalassistant using their personal credentials.
    
secure Class
------------

.. autoclass:: pypersonalassistant.secure.secure

Methods
^^^^^^^

An instance of the :py:class:`~pypersonalassistant.secure.secure` class has the following
methods.

Email
"""""

.. automethod:: pypersonalassistant.secure.secure.gmail_email
.. automethod:: pypersonalassistant.secure.secure.email
.. automethod:: pypersonalassistant.secure.secure.email_me

SMS
"""

.. automethod:: pypersonalassistant.secure.secure.twilio_SMS
.. automethod:: pypersonalassistant.secure.secure.SMS
.. automethod:: pypersonalassistant.secure.secure.SMS_me

Raw credentials
"""""""""""""""

.. automethod:: pypersonalassistant.secure.secure.credential
.. automethod:: pypersonalassistant.secure.secure.edit_credentials

Attributes
^^^^^^^^^^

.. py:attribute:: secure.credentials_path

    The path to the file containing encrypted personal credentials

    :type: string
