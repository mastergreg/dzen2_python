#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from signal import signal, alarm, SIGALRM
from subprocess import Popen,PIPE
from sys import stdin as SysStdin,stdout as SysStdout,stderr as SysStderr
from os import system,getenv
from re import sub
from config_mod import replace_p,XMONAD_PERCENTAGE, TEXT_COLOR, BACKGROUND_COLOR, FONT, TIME_COLOR, TIME_BACKGROUND_COLOR, SCREEN_PERCENTAGE, RUN_ORDER 
import dzen_size
#import torrentflux
logfile = open(getenv('HOME')+'/.dzen_python.log','a')
SysStdout = logfile
errorfile = open(getenv('HOME')+'/.dzen_python.errors','a')
SysStderr = errorfile 



def initialize():
    global cpu,ram,hddtemp,battery,time_mod,weather,mpd_mod,dmesg,gmail_check,cputemp,statusnet,volume_mod,keyboard

    if 'cpu' in RUN_ORDER:
        cpu=__import__('cpu',globals(),locals(),['cpu','get_cpu'],-1)
        cpu.get_cpu().start()
    if 'ram' in RUN_ORDER:
        ram=__import__('ram',globals(),locals(),['ram','get_ram'],-1)
        ram.get_ram().start()
    if 'hddtemp' in RUN_ORDER:
        hddtemp=__import__('hddtemp',globals(),locals(),['hddtemp','get_hddtemp'],-1)
        hddtemp.get_hddtemp().start()
    if 'battery' in RUN_ORDER:
        battery=__import__('battery',globals(),locals(),['cpu','get_battery'],-1)
        battery.get_battery().start()
    if 'time' in RUN_ORDER:
        time_mod=__import__('time_mod',globals(),locals(),['NOW'],-1)
    if 'weather' in RUN_ORDER:
        weather=__import__('weather',globals(),locals(),['weather_cond','get_weather'],-1)
        weather.get_weather().start()
    if 'dmesg' in RUN_ORDER:
        dmesg=__import__('dmesg',globals(),locals(),['dmesg','get_dmesg'],-1)
        dmesg.get_dmesg().start()
    if 'gmail' in RUN_ORDER:
        gmail_check=__import__('gmail_check',globals(),locals(),['unread','get_gmail_check'],-1)
        gmail_check.get_gmail_check().start()
    if 'cputemp' in RUN_ORDER:
        cputemp=__import__('cputemp',globals(),locals(),['cputemp','get_cputemp'],-1)
        cputemp.get_cputemp().start()
    if 'statusnet' in RUN_ORDER:
        statusnet=__import__('statusnet',globals(),locals(),['statusnet','get_statusnet'],-1)
        statusnet.get_statusnet().start()
    if 'mpd_song' in RUN_ORDER:
        mpd_mod=__import__('mpd_mod',globals(),locals(),['song','get_mpd'],-1)
        mpd_mod.get_mpd().start()
    if 'volume' in RUN_ORDER:
        volume_mod=__import__('volume_mod',globals(),locals(),['volume','get_volume'],-1)
        volume_mod.get_volume().start()
    if 'keyboard' in RUN_ORDER:
        keyboard=__import__('keyboard_mod',globals(),locals(),['layout','get_layout'],-1)
        keyboard.get_layout().start()

def split():
    return "^pa("+str(float(dzen_size.DZEN_SIZE)*float(XMONAD_PERCENTAGE))+")"

def get_data(p):
    data_list=[]
    data_dict={ 'xmonad'        :   "replace_p(p)", 
                'split'         :   "split()",
                'cpu'           :   "cpu.cpu()",
                'ram'           :   "ram.ram()",
                'hddtemp'       :   "hddtemp.hddtemp()",
                'battery'       :   "battery.battery()",
                'time'          :   "time_mod.NOW()",
                'weather'       :   "weather.weather_cond()" , 
                'mpd_song'      :   "mpd_mod.song()",
                'dmesg'         :   "dmesg.dmesg()",
                'gmail'         :   "gmail_check.unread()",
#                'torrentflux'  :   "torrentflux.SPEEDS",
                'cputemp'       :   "cputemp.cputemp()",
      		    'statusnet'     :   "statusnet.statusnet()",
                'volume'        :   "volume_mod.volume()", 
                'keyboard'      :   "keyboard.layout()"  }
      		
    for i in RUN_ORDER:
        j = eval(data_dict[i])
        data_list.append(j)
    data = " ".join(data_list)
    data = data.replace("\n","")
    return '^tw()'+data+"\n"

def handler(signum,frame):
    return


def main():
    initialize()
    """INNER SPACES"""

    """LAUNCH DZEN"""
    proc = Popen('dzen2 -w '+dzen_size.DZEN_SIZE+' -fg '+TEXT_COLOR+' -bg '+BACKGROUND_COLOR+' -ta l -fn '+FONT, 
                            shell=True, 
                            stdin=PIPE
                            )
    (child_stdin, child_stdout) = (proc.stdin, proc.stdout)
    signal(SIGALRM,handler)
    p=""

    """MAIN LOOP"""

    while True:
        alarm(1)
        try:
            p=SysStdin.readline()
            p=p.replace('\n','')
            data=get_data(p)
            child_stdin.write(data)
            continue
        except:
            data=get_data(p)
            child_stdin.write(data)
            continue

if __name__ == "__main__":
    main()
