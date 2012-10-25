#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : wifi.py
# Creation Date : 15-10-2012
# Last Modified : Tue 16 Oct 2012 05:13:30 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

from threading import Thread
from config_mod import WIFI_SLEEP,WIFI_IFACE
from time import sleep
from colors import set_normal_color, set_measure_color, set_gradient_color
from icons import set_icon
import socket
import os



WIFI=set_icon("net-wifi.xbm")
WIFI_SLEEP = int(WIFI_SLEEP)
ctl_iface = "/var/run/wpa_supplicant/" + WIFI_IFACE

def set_wifi(status):
    global WIFI
    WIFI = "{0}{1}".format(set_icon("net-wifi.xbm"), status)

def get_wifi():
    return WIFI
def get_ssid(status):
    status = dict([ map(lambda y: str(y), x.split('=')) for x in str(status)[2:].strip("'").split("\\n") if x])
    if status['wpa_state'] == 'COMPLETED':
        return status['ssid']
    else:
        return status['wpa_state']

class wifi(Thread):
    def run(self):
        global WIFI,WIFI_SLEEP, ctl_iface
        soc = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM, 0)
        soc.bind("/tmp/wpa_supplicant"+str(os.getpid()))
        soc.connect(ctl_iface)
        while True:
            soc.sendall(b'STATUS')
            status, ctl_file = soc.recvfrom(1024)
            ssid = get_ssid(status)
            set_wifi(ssid)
            sleep(WIFI_SLEEP)

def main():
    pass

if __name__ == "__main__":
    main()

