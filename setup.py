#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : setup.py
#
#* Purpose :
#
#* Creation Date : 19-10-2011
#
#* Last Modified : Wed 19 Oct 2011 08:19:04 AM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/




import os
from setuptools import setup

from dzen_python import dzen_python

setup(
    name = "Dzen_Python",
    version = dzen_python.VERSION,
    author = "Greg Liras",
    author_email = "gregliras@gmail.com",
    description = "OSD using dzen to provide system information",
    license = "GPL",
    keywords = "xmonad,dzen,python,OSD",
    url="https://github.com/mastergreg/dzen_python",
    packages=['dzen_python'],
    classifiers = [
      "Topic :: System Administration :: Monitoring",
      "Development Status :: 4 - Beta",
      "License :: Freely Distributable",
      "License :: OSI Approved :: GNU General Public License (GPL)"
      ],
    entry_points = {
      'console_scripts': ['dzen_python = dzen_python.dzen_python']
      },
    data_files = [
      ('dzen_python.py', ['README']),
      ]
    )
