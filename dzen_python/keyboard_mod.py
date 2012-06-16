from time import sleep
from threading import Thread
from subprocess import Popen,PIPE
from config_mod import KB_COLOR, KB_BACKGROUND_COLOR
from colors import set_colors,set_normal_color


LAYOUT=""

def layout():
    return LAYOUT

class get_layout(Thread):
    def run(self):
        global LAYOUT
        while True:
            res_proc= Popen("setxkbmap -print | grep xkb_symbols",shell=True,stdout=PIPE)
            res = res_proc.stdout
            inp = res.read().decode().strip()
            LAYOUT = set_colors(KB_COLOR, KB_BACKGROUND_COLOR)+inp.split('+')[1].upper()+set_normal_color()
                
            sleep(1)
