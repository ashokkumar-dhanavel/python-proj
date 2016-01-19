try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'logfind',
    'author': 'Ashok',
    'url': 'https://github.com/ashokkumar-dhanavel/python-proj.git',
    'download_url': 'https://github.com/ashokkumar-dhanavel/python-proj.git',
    'author_email': 'ashok@5gindia.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': ['bin/logfind'],
    'name': 'logfind'
}

setup(**config)
