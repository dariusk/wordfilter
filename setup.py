#!/usr/bin/env python
import os
from setuptools import setup

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
    )
    return open(file_path).read()

setup(
    name=u'wordfilter',

    version='0.1.7',

    description="A small module meant for use in text generators that lets you filter strings for bad words.",

    long_description=read_file('README.md'),

    author=u'Darius Kazemi',

    author_email=u'darius.kazemi@gmail.com',

    url='http://tinysubversions.com',

    license=read_file('LICENSE-MIT'),

    packages=['wordfilter'],

    zip_safe=False,

    data_files=[
        ('wordfilter', ['lib/badwords.json']),
    ],

    classifiers=[
        "Programming Language :: Python",
    ],
)
