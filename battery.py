from threading import Thread
from time import sleep
from colors import set_measure_color,set_normal_color
from config_mod import BATTERY_NAME, ICON_PATH
from pynotify import init as notiftinit,Notification,URGENCY_NORMAL,EXPIRES_NEVER
BATTERY=""
def battery():
  return BATTERY
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
          notiftinit("dzen_python")
          n = pynotify.Notification("Battery Status", "Low Battery", "Your Battery Is Low")
          n.set_urgency(pynotify.URGENCY_NORMAL)
          n.set_timeout(pynotify.EXPIRES_NEVER)
          n.show()
        BATTERY="^i(/home/master/.icons/dzen2/power-bat.xbm)"+set_measure_color(100-percent)+str(percent)+set_normal_color()+"%"
        f1.close()
        f2.close()
      except IOError:
        try:
          f1=open('/proc/acpi/battery/'+BATTERY_NAME+'/state','r')
          f2=open('/proc/acpi/battery/'+BATTERY_NAME+'/info','r')
          f1lines=f1.readlines()
          f2lines=f2.readlines()
          for i in f1lines:
            if i.startswith("remaining capacity"):
              current=i.split()[2]
          for i in f2lines:
            if i.startswith("last full capacity"):
              full=i.split()[2]
          BATTERY=" ^i("+ICON_PATH+"/power-bat.xbm)"+set_measure_color(100-percent)+str(percent)+set_normal_color()+"%"
          f1.close()
          f2.close()
        except:
          BATTERY=" NoBat"
      sleep(60)
