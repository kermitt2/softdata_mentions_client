#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    reqs = f.readlines()

setup(name='softdata_mentions_client',
      version='0.0.1',
      description='Python client for using the Softcite software mention recognition service and the DataStet dataset mention recognition service',
      author='kermitt2',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=reqs,
      license='LICENSE',
    )
