from threading import Thread
from psutil import used_phymem,TOTAL_PHYMEM
from config_mod import RAM_SLEEP 
from time import sleep
from colors import set_normal_color, set_measure_color

RAM=""
class get_mem(Thread):
  def run(self):
    global RAM,RAM_SLEEP
    while 1:
      used=bytes_to_mb(used_phymem()-cached_mem()-buffers())
      percentage=(100*used)/TOTAL_RAM_MB
      RAM=" ^i(/home/master/.icons/dzen2/mem.xbm) "+set_measure_color(percentage)+str(used)+set_normal_color()+"M"
      sleep(int(RAM_SLEEP))
def bytes_to_mb(byte):
  return byte/1048576
def cached_mem():
  """Return the amount of cached memory on the system, in bytes."""
  f = open('/proc/meminfo', 'r')
  for line in f:
    if line.startswith('Cached:'):
      f.close()
      return int(line.split()[1]) * 1024
def cached_swap():
  """Return the amount of cached swap on the system, in bytes."""
  f = open('/proc/meminfo', 'r')
  for line in f:
    if line.startswith('SwapCached:'):
      f.close()
      return int(line.split()[1]) * 1024
def buffers():
  """Return the amount of buffers on the system, in bytes."""
  f = open('/proc/meminfo', 'r')
  for line in f:
    if line.startswith('Buffers:'):
      f.close()
      return int(line.split()[1]) * 1024
TOTAL_RAM=TOTAL_PHYMEM
TOTAL_RAM_MB=bytes_to_mb(TOTAL_RAM)
