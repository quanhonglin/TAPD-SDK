#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='tapd-sdk',
    version='1.0.0',
    url='http://gitlab.rd.175game.com/platform/TAPD-SDK.git',
    description='TAPD service python driver',
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'requests>=2.2.1',
    ],
)
