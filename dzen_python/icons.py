#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : icons.py
# Creation Date : 16-10-2012
# Last Modified : Tue 16 Oct 2012 09:43:04 AM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from config_mod import ICON_PATH

def set_icon(iconfile):
    return "^i({0}/{1}) ".format(ICON_PATH, iconfile)

