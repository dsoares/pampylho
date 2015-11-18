#!/usr/bin/env python
"""
An interface to the Pluggable Authentication Modules (PAM) library,
written in pure Python (using ctypes).
"""

import io
import os
import sys

from distutils.core import setup

if 'bdist_wheel' in sys.argv:
    import setuptools

with open('pampylho.py') as f:
    for line in f:
        if line.startswith('__version__'):
            version_ns = {}
            exec(line, version_ns)
            version = version_ns['__version__']

setup(name='pampylho',
      version=version,
      description="PAM interface using ctypes",
      long_description=__doc__,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
          "Operating System :: MacOS :: MacOS X",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Systems Administration :: Authentication/Directory"
          ],
      keywords=['pam', 'authentication'],
      author='Diana Soares',
      author_email='diana.soares@gmail.com',
      url='http://github.com/dsoares/pampylho',
      license='MIT',
      py_modules=["pampylho"],
  )
