#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='addtask',
    version='0.1',
    description='Add tasks to Google Tasks with natural language',
    author='Carey Metcalfe',
    author_email='pR0Ps.CM@gmail.com',
    url='https://github.com/pR0Ps/addtask',
    scripts=['addtask'],
    install_requires=[
        "google-api-python-client",
        "parsedatetime",
    ],
)
