#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
 
setup(
	name="PackageName",
	ext_modules=[
		Extension("my_booster", ["gmp_factorial.cpp", "booster.cpp"],
		libraries = ["gmp", "boost_python"])
	]
)
