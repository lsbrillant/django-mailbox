from distutils.core import setup

setup(
    name='django-mailbox',
    version='1.1.1',
    url='http://bitbucket.org/latestrevision/django-mailbox/',
    description='Automatically import mail from POP3, IMAP, or a local mailbox into Django',
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=[
        'django_mailbox',
        'django_mailbox.management',
        'django_mailbox.management.commands',
        'django_mailbox.migrations',
        'django_mailbox.transports',
        ],
)
