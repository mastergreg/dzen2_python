from threading import Thread
from time import sleep
BATTERY=""
class get_battery(Thread):
  def run(self):
    global BATTERY
    while True:
      f1 = open('/sys/class/power_supply/CMB1/charge_full','r')
      f2 = open('/sys/class/power_supply/CMB1/charge_now','r')
      full=float(f1.readline())
      current=float(f2.readline())
      BATTERY=" ^i(/home/master/.icons/dzen2/power-bat.xbm)"+str(int(current*100/full))+"%"
      f1.close()
      f2.close()
      sleep(60)
