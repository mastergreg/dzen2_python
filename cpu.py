from threading import Thread
from config_mod import CPU_SLEEP
from colors import set_measure_color, set_normal_color 
from time  import sleep
from psutil import cpu_percent

  
CPU=""
class get_cpu(Thread):
  def run(self):
    MAX_FREQ=0
    MIN_FREQ=999999
    while 1:
      global CPU,CPU_SLEEP
      f = open('/proc/cpuinfo', 'r')
##      cpu_frequencies=""
      freqs=[]
      for line in f:
        if line.startswith('cpu MHz'):
          freqs.append(int(round(float(line.split()[3]),0)))
      f.close()
##      for i in range (len(freqs)):
##        cpu_frequencies+=" Core"+str(i)+"@ "+str(freqs[i])
      freq=max(freqs)
      if MAX_FREQ<freq:
        MAX_FREQ=freq
      fpercentage=100*freq/MAX_FREQ
      cpu_frequencies=" @ "+set_measure_color(fpercentage)+str(round(freq/1000.,1))+set_normal_color()+"GHz"
      percentage=round(cpu_percent(), 1)
      CPU=" ^i(/home/master/.icons/dzen2/cpu.xbm) "+set_measure_color(percentage)+str(percentage)+set_normal_color()+"%"+cpu_frequencies
      sleep(int(CPU_SLEEP))
