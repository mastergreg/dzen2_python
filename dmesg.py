from threading import Thread
from time import sleep
from subprocess import Popen,PIPE

DMESG=""
class get_dmesg(Thread):
  def run(self):
    global DMESG
    while True:
      dmesg_proc= Popen("dmesg | tail -n 10",shell=True,stdout=PIPE)
      DMESG=dmesg_proc.stdout.read()
      sleep(5)
