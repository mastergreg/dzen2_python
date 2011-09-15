from time import sleep
import threading
import re
import urllib2
from config_mod import WEATHER_BACKGROUND_COLOR, WEATHER_COLOR, WEATHER_SLEEP, REQ
from colors import *
WEATHER_COND=""

def weather_cond():
  return WEATHER_COND
class get_weather(threading.Thread):
  def run ( self ):
    global WEATHER_COND,WEATHER_SLEEP,REQ
    
    while True:
      try:
        request = urllib2.Request(REQ)
        response = urllib2.urlopen(request)
        the_page = response.read()
        result= re.search('e:.*?C',the_page)
        result_sum = re.search('"summary">.*?<',the_page)
        WEATHER_COND=' '+set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+result_sum.group(0)[10:len(result_sum.group(0))-2]+ result.group(0)[2:len(result.group(0))-6]+"C"+set_normal_color()
        sleep(float(WEATHER_SLEEP))
        continue
      except (urllib2.URLError,AttributeError):
        WEATHER_COND=' '+set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+"No Net"+set_normal_color()
        sleep(60)
        continue
