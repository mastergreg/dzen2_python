#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : wifi.py
# Creation Date : 15-10-2012
# Last Modified : Mon 15 Oct 2012 01:56:37 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from threading import Thread
from config_mod import WIFI_SLEEP,WIFI_IFACE,ICON_PATH 
from time import sleep
from colors import set_normal_color, set_measure_color, set_gradient_color
import socket
import os



WIFI="^i("+ICON_PATH+"/net-wifi.xbm) "
WIFI_SLEEP = int(WIFI_SLEEP)
ctl_iface = "/var/run/wpa_supplicant/" + WIFI_IFACE

def set_wifi(status):
    global WIFI
    WIFI = "^i("+ICON_PATH+"/net-wifi.xbm) " + status

def get_wifi():
    return WIFI
def get_ssid(status):
    lines = str(status[0]).strip("'").split("\\n")
    a = lines[1].split('=')[1]
    return a

class wifi(Thread):
    def run(self):
        global WIFI,WIFI_SLEEP, ctl_iface
        soc = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM, 0)
        soc.bind("/tmp/wpa_supplicant"+str(os.getpid()))
        soc.connect(ctl_iface)
        while True:
            soc.sendall(b'STATUS')
            status = soc.recvfrom(1024)
            ssid = get_ssid(status)
            set_wifi(ssid)
            sleep(WIFI_SLEEP)

def main():
    pass

if __name__ == "__main__":
    main()

