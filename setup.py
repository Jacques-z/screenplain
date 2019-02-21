#!/usr/bin/env python

from distutils.core import setup

setup(
    name='screenplain',
    version='0.8.0',
    description='Convert text file to viewable screenplay.',
    author='Martin Vilcans',
    author_email='screenplain@librador.com',
    url='http://www.screenplain.com/',
    install_requires=[
        'six',
    ],
    extras_require={
        'PDF': 'reportlab'
    },
    packages=[
        'screenplain',
        'screenplain.export',
        'screenplain.parsers',
    ],
    package_data={
        'screenplain.export': ['default.css']
    },
    scripts=[
        'bin/screenplain'
    ]
)
