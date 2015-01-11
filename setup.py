from setuptools import setup

import traceback
import glim_extensions
import os

from os.path import exists

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

try:
    from setuptools import setup, find_packages
except ImportError:
	print(traceback.format_exc())

setup(
    author='Aras Can Akin',
    author_email='aacanakin@gmail.com',
    name='glim-extensions',
    packages=find_packages(),
    version=glim_extensions.version,
    description='Glim Extensions',
    long_description=read('README.rst'),
    url='https://github.com/aacanakin/glim-extensions',
    download_url='https://github.com/aacanakin/glim-extensions/archive/v%s.zip' % glim_extensions.version,
    keywords=[
        'framework',
        'web framework',
        'extensions',
        'redis',
        'job queue',
        'SQLAlchemy',
        'Jinja2',
        'mail queue'
    ],
    install_requires=[
		"glim",
        "SQLAlchemy",
		"Jinja2",
        "pymemcache",
        "redis"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
