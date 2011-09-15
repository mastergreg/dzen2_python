from threading import Thread
from config_mod import HDDTEMP_SLEEP,ICON_PATH
from socket import socket, AF_INET,SOCK_STREAM
from colors import set_normal_color, set_measure_color
from time import sleep
HDDTEMP=""


def hddtemp():
  return HDDTEMP
class get_hddtemp(Thread):
  def run(self):
    global HDDTEMP,HDDTEMP_SLEEP
    while 1:
      s = socket(AF_INET, SOCK_STREAM)
      s.connect(("localhost",7634))
      buf = s.recv(4096)
      s.close()
      temp=buf[len(buf)-5:len(buf)-3]
      try:
        percentage=100*(int(temp)-20)/40
      except ValueError:
        continue
      HDDTEMP=" ^i("+ICON_PATH+"/temp.xbm) "+set_measure_color(percentage)+temp+set_normal_color()+"C"
      sleep(int(HDDTEMP_SLEEP))

