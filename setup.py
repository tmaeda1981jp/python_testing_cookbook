#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

# setup(
#     name="RegexPicker plugin",
#     version="0.1",
#     author="tmaeda1981jp",
#     author_email="tmaeda1981jp at gmail",
#     description="Pick test methods based on a regular expression",
#     license="Apache Server Licence 2.0",
#     py_modules=["recipe13_plugin"],
#     entry_points = {
#         'nose.plugins': [
#             'recipe13_plugin = recipe13_plugin:RegexPicker'
#         ]
#     }
# )
setup(
    name="CSV report plugin",
    version="0.1",
    author="tmaeda1981jp",
    author_email="tmaeda1981jp at gmail",
    description="Generate CSV report",
    license="Apache Server Licence 2.0",
    py_modules=["recipe14_plugin"],
    entry_points = {
        'nose.plugins': [
            'recipe14_plugin = recipe14_plugin:CsvReport'
        ]
    }
)
