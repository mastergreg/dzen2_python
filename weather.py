from time import sleep
import threading
import re
import urllib2
from config_mod import WEATHER_BACKGROUND_COLOR, WEATHER_COLOR, WEATHER_SLEEP, REQ
from colors import *
WEATHER_COND=""
class get_weather(threading.Thread):
  def run ( self ):
    global WEATHER_COND,WEATHER_SLEEP,REQ
    while True:
      try:
        response = urllib2.urlopen(REQ)
        the_page = response.read()
        result= re.search('::.*?<',the_page)
        WEATHER_COND=' '+set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+result.group(0)[2:len(result.group(0))-1]+set_normal_color()
        sleep(float(WEATHER_SLEEP))
        continue
      except (urllib2.URLError,AttributeError):
        WEATHER_COND=' '+set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+"No Net"+set_normal_color()
        sleep(10.0)
        continue
