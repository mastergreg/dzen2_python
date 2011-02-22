import threading
import ConfigParser
from time import sleep
config = ConfigParser.RawConfigParser()
config.readfp(open('.dzen_pythonrc'))
config.get('main_config','HIDDEN_BACKGROUND_COLOR')

"""GLOBAL VARIBLES OF CONFIGURATION"""

TEXT_COLOR=config.get('main_config','TEXT_COLOR')
BACKGROUND_COLOR=config.get('main_config','BACKGROUND_COLOR')
CURRENT_TEXT_COLOR=config.get('main_config','CURRENT_TEXT_COLOR')
CURRENT_BACKGROUND_COLOR=config.get('main_config','CURRENT_BACKGROUND_COLOR')
VISIBLE_TEXT_COLOR=config.get('main_config','VISIBLE_TEXT_COLOR')
VISIBLE_BACKGROUND_COLOR=config.get('main_config','VISIBLE_BACKGROUND_COLOR')

HIDDEN_TEXT_COLOR=config.get('main_config','HIDDEN_TEXT_COLOR')
HIDDEN_BACKGROUND_COLOR=config.get('main_config','HIDDEN_BACKGROUND_COLOR')

HIDDEN_NO_WINDOWS_TEXT_COLOR=config.get('main_config','HIDDEN_NO_WINDOWS_TEXT_COLOR')
HIDDEN_NO_WINDOWS_BACKGROUND_COLOR=config.get('main_config','HIDDEN_NO_WINDOWS_BACKGROUND_COLOR')

URGENT_TEXT_COLOR=config.get('main_config','URGENT_TEXT_COLOR')
URGENT_BACKGROUND_COLOR=config.get('main_config','URGENT_BACKGROUND_COLOR')

TITLE_TEXT_COLOR=config.get('main_config','TITLE_TEXT_COLOR')
TITLE_BACKGROUND_COLOR=config.get('main_config','TITLE_BACKGROUND_COLOR')

LAYOUT_TEXT_COLOR=config.get('main_config','LAYOUT_TEXT_COLOR')
LAYOUT_BACKGROUND_COLOR=config.get('main_config','LAYOUT_BACKGROUND_COLOR')

MEASURE_NORMAL_COLOR=config.get('main_config','MEASURE_NORMAL_COLOR')
MEASURE_MEDI_COLOR=config.get('main_config','MEASURE_MEDI_COLOR')
MEASURE_HIGH_COLOR=config.get('main_config','MEASURE_HIGH_COLOR')
FONT=config.get('main_config','FONT')
#-misc-fixed-medium-r-normal--12-*-*-*-*-*-iso8859-1'
# -*-terminus-*-r-normal-*-13-120-*-*-*-*-iso8859-*
RUN_ORDER=["XMONAD","CPU","MEM","WEATHER","DATE"]
REQ = config.get('main_config','REQ')
p=""


TIME_COLOR=config.get('main_config','TIME_COLOR')
TIME_BACKGROUND_COLOR=config.get('main_config','TIME_BACKGROUND_COLOR')
#FFFF66"
"""WEATHER STUFF"""
WEATHER_SLEEP=config.get('main_config','WEATHER_SLEEP')
WEATHER_COLOR=config.get('main_config','WEATHER_COLOR')
WEATHER_BACKGROUND_COLOR=config.get('main_config','WEATHER_BACKGROUND_COLOR')
#WEATHER_COND=""
"""TEMPERATURE STUFF"""
HDDTEMP_SLEEP=config.get('main_config','HDDTEMP_SLEEP')
HDDTEMP=""
"""SYSTEM PERFORMANCE STUFF"""
CPU_SLEEP=config.get('main_config','CPU_SLEEP')
CPU=""
RAM_SLEEP=config.get('main_config','RAM_SLEEP')
RAM=""
BATTERY=""

"""MPD STATUS"""
HOSTS = config.get('main_config','MPD_HOST').split()
PORT = config.get('main_config','MPD_PORT')
#SONG ="" 




findandreplace=[
  ['#000001',CURRENT_TEXT_COLOR]
, ['#000010',CURRENT_BACKGROUND_COLOR]
, ['#000002',VISIBLE_TEXT_COLOR]
, ['#000020',VISIBLE_BACKGROUND_COLOR]
, ['#000003',HIDDEN_TEXT_COLOR]
, ['#000030',HIDDEN_BACKGROUND_COLOR]
, ['#000004',HIDDEN_NO_WINDOWS_TEXT_COLOR]
, ['#000040',HIDDEN_NO_WINDOWS_BACKGROUND_COLOR]
, ['#000005',URGENT_TEXT_COLOR]
, ['#000050',URGENT_BACKGROUND_COLOR]
, ['#000006',TITLE_TEXT_COLOR]
, ['#000060',TITLE_BACKGROUND_COLOR]
, ['#000007',LAYOUT_TEXT_COLOR]
, ['#000070',LAYOUT_BACKGROUND_COLOR]
]






