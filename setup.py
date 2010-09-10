#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ja.is-sms',
    version='0.1',
    author='Stefan Kjartansson',
    author_email='esteban.supreme@gmail.com',
    url='http://www.ja.is',
    description = 'SMS sending',
    packages=find_packages(),
    install_requires=[
    ],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
