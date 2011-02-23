
from config_mod import replace_p,RUN_ORDER 
import mpd_mod
import weather
import cpu
import ram
import hddtemp
import battery
import time_mod
import dmesg



def get_data(p):
  data_list=[]
  data_dict={}
  data_dict={ 'xmonad': replace_p(p),
              'cpu' : cpu.CPU,
              'ram' : ram.RAM,
              'hddtemp' : hddtemp.HDDTEMP,
              'battery' : battery.BATTERY,
              'time' : time_mod.NOW(),
              'weather':weather.WEATHER_COND , 
              'mpd_song' : mpd_mod.SONG , 
              'break_line':'\n',
              'dmesg' : dmesg.DMESG}
  for i in RUN_ORDER:
    data_list.append(data_dict[i])
  return ''.join(data_list)
