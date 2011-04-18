from threading import Thread
from time import sleep
from subprocess import Popen,PIPE
from colors import set_measure_color,set_normal_color
from config_mod import BATTERY_NAME
from pynotify import Notification,URGENCY_NORMAL,EXPIRES_NEVER
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
          n = pynotify.Notification("Battery Status", "Low Battery", "Your Battery Is Low")
          n.set_urgency(pynotify.URGENCY_NORMAL)
          n.set_timeout(pynotify.EXPIRES_NEVER)
          n.show()
        BATTERY=" ^i(/home/master/.icons/dzen2/power-bat.xbm)"+set_measure_color(100-percent)+str(percent)+set_normal_color()+"%"
        f1.close()
        f2.close()
      except:
        BATTERY=" NoBat"
      sleep(60)
