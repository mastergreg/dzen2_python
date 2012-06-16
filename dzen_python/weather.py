from time import sleep
from threading import Thread
from re import search
from urllib.request import Request, urlopen, URLError
from config_mod import WEATHER_BACKGROUND_COLOR, WEATHER_COLOR, WEATHER_SLEEP, REQ
from colors import set_colors,set_normal_color
WEATHER_COND=set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+"n/a"+set_normal_color()

def weather_cond():
    return WEATHER_COND
class get_weather(Thread):
    def run ( self ):
        global WEATHER_COND,WEATHER_SLEEP,REQ
    
        while True:
            try:
                request = Request(REQ)
                response = urlopen(request)
                the_page = response.read().decode()
                result= search('e:.*?C',the_page)
                result_sum = search('"summary">.*?<',the_page)
                WEATHER_COND=set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+result_sum.group(0)[10:len(result_sum.group(0))-2]+ result.group(0)[2:len(result.group(0))-6]+"C"+set_normal_color()
                sleep(float(WEATHER_SLEEP))
                continue
            except (URLError,AttributeError):
                WEATHER_COND=set_colors(WEATHER_COLOR,WEATHER_BACKGROUND_COLOR)+"n/a"+set_normal_color()
                sleep(60)
                continue
