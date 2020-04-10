#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='ariadne_spike',
    version='1.0.0',
    packages=find_packages(exclude=["*_tests"]),
    license='MIT license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points = {
        'console_scripts': [
            'ariadne_spike = ariadne_spike.cli:cli',
        ],
    },
    install_requires = [
        'ariadne',
        'click',
        'decorator',
        'flask',
        'uvicorn'
    ],
    extras_require={
        'dev': [
            'pylint',
            'coverage',
            'tox',
            'twine'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Console"
    ]
)
