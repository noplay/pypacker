#!/usr/bin/env python

import pypacker

from distutils.core import setup
#import setuptools

setup(name="pypacker",
	version="1.9",
	author="Michael Stahn",
	author_email="michael.stahn.42(at)gmail.com",
	url="https://github.com/mike01/pypacker",
	description="pypacker: Fast and simple packet creation and parsing module",
	license="BSD",
	packages=[ "pypacker",
		"pypacker.layer12",
		"pypacker.layer3",
		"pypacker.layer4",
		"pypacker.layer567"]
	)