Communication: simple, secure messaging
=======================================

Send some emails
^^^^^^^^^^^^^^^^

The following script allows a user to enter a master password before starting a long task,
authorising later use of their email (`gmail`_) account.

.. _gmail: https://mail.google.com/

.. code-block:: python

    import pypersonalassistant.secure

    ppa_secure = pypersonalassistant.secure.secure()
    results = some_long_task(foo, bar)
    recipients = ['my.boss@company.com',
                  'coworker.one@company.com',
                  'coworker.two@company.com'
                  ]
    content = 'Subject: Results of my task\n{0}'.format(results)
    for r in recipients:
        ppa_secure.email(r, content)

Send an SMS
^^^^^^^^^^^

Or send SMS messages using (`twilio`_).
   
.. _twilio: https://www.twilio.com/

.. code-block:: python

    import pypersonalassistant.secure

    ppa_secure = pypersonalassistant.secure.secure()
    some_long_task(foo, bar)
    ppa_secure.SMS_me('Task completed')
