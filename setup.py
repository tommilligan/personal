from setuptools import setup

setup(name='pypersonalassistant',
      version='0.1.2',
      description='Easy, secure self notification via email and sms, using smtplib and twilio',
      long_description='Using pycrypto AES, personal credentials such as passwords and tokens are encrypted and persistently stored, to allow later automatic notification without a person present. User authentication with a master password is required at object initialisation',
      url='https://github.com/tommilligan/personal',
      author='Tom Milligan',
      author_email='code@tommilligan.net',
      license='GPL',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
      ],
      keywords='personal automation automatic notification email sms text secure',
      packages=['pypersonalassistant'],
      install_requires=[
          'pycrypto',
          'twilio',
      ],
      entry_points={
        'console_scripts': [
            'pypersonalassistant-credentials = pypersonalassistant.ppa_secure:main'
        ]
      }
)