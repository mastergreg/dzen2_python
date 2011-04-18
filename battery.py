from threading import Thread
from time import sleep
from subprocess import Popen,PIPE
from colors import set_measure_color,set_normal_color
from config_mod import BATTERY_NAME
BATTERY=""
class get_battery(Thread):
  def run(self):
    global BATTERY
    while True:
      try:
        f1 = open('/sys/class/power_supply/'+BATTERY_NAME+'/charge_full','r')
        f2 = open('/sys/class/power_supply/'+BATTERY_NAME+'/charge_now','r')
        full=float(f1.readline())
        current=float(f2.readline())
        percent=int(current*100/full)
        if percent>100:
          percent=100
        elif percent<9:
          battery_notification().start()
        BATTERY=" ^i(/home/master/.icons/dzen2/power-bat.xbm)"+set_measure_color(100-percent)+str(percent)+set_normal_color()+"%"
        f1.close()
        f2.close()
      except:
        BATTERY=" NoBat"
      sleep(60)
class battery_notification(Thread):
  def run(self):
    while True:
      notif=Popen("dzen2 -fn '-misc-fixed-bold-r-semicondensed--13-90-100-100-c-60-iso8859-1' -w 150 -x 400 -y 300 -bg black -fg red",shell=True,stdin=PIPE)
      notif.stdin.write("LOW BATTERY\n")
      sleep(1)
      notif.send_singal(SIGKILL)
      sleep(1)

