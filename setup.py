# Copyright 2014 icasdri
__author__ = 'icasdri'

from user_python_daemon.user_python_daemon import VERSION, DESCRIPTION
from distutils.core import setup

setup(
    name='pybatterymonitor',
    version=str(VERSION),
    license='GPL3',
    author='icasdri',
    author_email='icasdri@gmail.com',
    description=DESCRIPTION,
    url='https://github.com/icasdri/user-python-daemon',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ],
    packages=['user_python_daemon'],
    scripts=['distributing/user-python-daemon']
)
