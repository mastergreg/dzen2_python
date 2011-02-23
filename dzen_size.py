from subprocess import Popen,PIPE
from config_mod import FONT,SCREEN_PERCENTAGE


def resolution():
  res_proc= Popen("xrandr  | grep \* | cut -d' ' -f4",shell=True,stdout=PIPE)
  res = res_proc.stdout
  return res.read().split()[0].split('x')
  


def get_font_size(font):
  return (int(font.split('-')[7])/2)+1
def len_dzen(my_string):
  new_string = sub('\^.*?\)','',my_string,0)
  return len(new_string) 
def dzen_string_length(p):
  return get_font_size(FONT)*len_dzen(p)

[SCREEN_WIDTH,SCREEN_HEIGHT]=resolution()
DZEN_SIZE=str(float(SCREEN_WIDTH)*float(SCREEN_PERCENTAGE))
