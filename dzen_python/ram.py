from threading import Thread
from config_mod import RAM_SLEEP,ICON_PATH 
from time import sleep
from colors import set_normal_color, set_measure_color, set_gradient_color

def free_mem():
    """Return the free amount  memory on the system, in bytes."""
    f = open('/proc/meminfo', 'r')
    for line in f:
        if line.startswith('MemFree:'):
            f.close()
            return int(line.split()[1]) * 1024
def total_mem():
    """Return the total amount of memory on the system, in bytes."""
    f = open('/proc/meminfo', 'r')
    for line in f:
        if line.startswith('MemTotal:'):
            f.close()
            return int(line.split()[1]) * 1024
def used_phymem():
    """Return the total amount of memory on the system, in bytes."""
    return total_mem()-free_mem()
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

def bytes_to_mb(byte):
    return byte//1048576
RAM=""
TOTAL_RAM=total_mem()
TOTAL_RAM_MB=bytes_to_mb(TOTAL_RAM)

def ram():
    return RAM
class get_ram(Thread):
    def run(self):
        global RAM,RAM_SLEEP
        while 1:
            used=bytes_to_mb(used_phymem()-cached_mem()-buffers())
            percentage=(100*used)/TOTAL_RAM_MB
            RAM="^i("+ICON_PATH+"/mem.xbm) "+set_gradient_color(percentage)+str(used)+set_normal_color()+"M"
            sleep(int(RAM_SLEEP))
