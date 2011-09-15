#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : cputemp.py
#
#* Purpose :
#
#* Creation Date : 15-09-2011
#
#* Last Modified : Thu 15 Sep 2011 09:56:04 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

from threading import Thread
from time import sleep
from config_mod import ICON_PATH
from colors import set_gradient_color,set_normal_color

CPUTEMP=""
class get_cpuTemp(Thread):
  def run(self):
    global CPUTEMP
    while True:
      try:
        f1 = open('/sys/devices/platform/coretemp.0/temp2_input','r')
        f2 = open('/sys/devices/platform/coretemp.0/temp3_input','r')
        TC1 = int(f1.readline())/1000
        TC2 = int(f2.readline())/1000
        C1ritical = int(open('/sys/devices/platform/coretemp.0/temp2_crit','r').readline())/1000
        C2ritical = int(open('/sys/devices/platform/coretemp.0/temp3_crit','r').readline())/1000
        percent1 = int(TC1*100/C1ritical)
        percent2 = int(TC2*100/C2ritical)
        if percent1 > 100:
          percent1 = 100
        if percent2 > 100:
          percent2 = 100
        CPUTEMP = " ^i("+ICON_PATH+"/temp.xbm) "+ set_gradient_color(100-percent1)+str(TC1)+set_normal_color()+" | "+set_gradient_color(100-percent2)+str(TC2)+set_normal_color()
        f1.close()
        f2.close()
      except IOError:
        CPUTEMP = "N/A"
      sleep(60);


