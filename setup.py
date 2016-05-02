#!/usr/bin/env python

"""
Package setup file for python module amitkrg.code.python
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='amitgupt.code.python',
    version='0.0.0',
    description='All python code used for daily purpose.',
    long_description=long_description,
    url='https://github.com/amit024003/CodePython',
    author='Amit Kumar Gupta',
    author_email='leave comment here.',
    license=''
    classifiers=[]
)
