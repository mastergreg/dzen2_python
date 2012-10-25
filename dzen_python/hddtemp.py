from threading import Thread
from config_mod import HDDTEMP_SLEEP
from socket import socket, AF_INET,SOCK_STREAM
from colors import set_normal_color, set_measure_color ,set_gradient_color
from time import sleep
from icons import set_icon
HDDTEMP=""


def hddtemp():
    return HDDTEMP
class get_hddtemp(Thread):
    def run(self):
        global HDDTEMP,HDDTEMP_SLEEP
        while 1:
            sleep(int(HDDTEMP_SLEEP))
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(("localhost",7634))
            buf = s.recv(4096)
            s.close()
            temp=str(buf).split("|")[3]
            try:
                percentage=100*(int(temp)-25)/60
            except ValueError:
                continue
            HDDTEMP=set_icon("temp.xbm")+set_gradient_color(percentage)+temp+set_normal_color()+"C"

