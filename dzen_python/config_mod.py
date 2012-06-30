# -*- coding: utf-8 -*-s
from configparser import RawConfigParser
from os import getenv

config = RawConfigParser()
config.readfp(open(getenv('HOME')+'/.dzen_pythonrc'))
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
RUN_ORDER=config.get('main_config','RUN_ORDER').split(',')
REQ = config.get('main_config','REQ')
p=""


TIME_COLOR=config.get('main_config','TIME_COLOR')
TIME_BACKGROUND_COLOR=config.get('main_config','TIME_BACKGROUND_COLOR')
#FFFF66"
"""WEATHER STUFF"""
WEATHER_SLEEP=config.get('main_config','WEATHER_SLEEP')
WEATHER_COLOR=config.get('main_config','WEATHER_COLOR')
WEATHER_BACKGROUND_COLOR=config.get('main_config','WEATHER_BACKGROUND_COLOR')
"""TEMPERATURE STUFF"""
HDDTEMP_SLEEP=config.get('main_config','HDDTEMP_SLEEP')
"""SYSTEM PERFORMANCE STUFF"""
CPU_BAR_COLOR=config.get('main_config','CPU_BAR_COLOR')
CPU_SLEEP=config.get('main_config','CPU_SLEEP')
RAM_SLEEP=config.get('main_config','RAM_SLEEP')

"""MPD STATUS"""
HOSTS = config.get('main_config','MPD_HOST').split(',')
PORT = config.get('main_config','MPD_PORT')

"""SCREEN"""
XMONAD_PERCENTAGE = config.get('main_config','XMONAD_PERCENTAGE')
SCREEN_PERCENTAGE = config.get('main_config','SCREEN_PERCENTAGE')


"""KEYBOARD"""
KB_COLOR=config.get('main_config','KB_COLOR')
KB_BACKGROUND_COLOR=config.get('main_config','KB_BACKGROUND_COLOR')



"""ICONS"""
ICON_PATH=config.get('main_config','ICON_PATH')
BATTERY_NAME=config.get('main_config','BATTERY_NAME')

STATUSNET_URL=config.get('main_config','STATUSNET_URL')

STATUSNET_COLOR=config.get('main_config','STATUSNET_COLOR')

STATUSNET_USER_COLOR=config.get('main_config','STATUSNET_USER_COLOR')

STATUSNET_BACKGROUND_COLOR=config.get('main_config','STATUSNET_BACKGROUND_COLOR')

GMAIL_BACKGROUND_COLOR=config.get('main_config','GMAIL_BACKGROUND_COLOR')
GMAIL_COLOR=config.get('main_config','GMAIL_COLOR')
GMAIL_UNREAD_COLOR=config.get('main_config','GMAIL_UNREAD_COLOR')

GMAIL_USERNAME=config.get('main_config','GMAIL_USERNAME')

GMAIL_PASSWORD=config.get('main_config','GMAIL_PASSWORD')

#TF_ADD=config.get('main_config','TF_ADD')
#TF_USER=config.get('main_config','TF_USER')
#TF_PASS=config.get('main_config','TF_PASS')

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






def replace_p(p):
  a = p  
  for couple in findandreplace:
    a=a.replace(couple[0],couple[1])
  #text = a.decode('utf-8', 'ignore')
  text = a.encode('iso-8859-7', 'ignore')

  from_chars = 'áâãäåæçèéêëìíîïðñóòôõö÷øùÜÝÞßúÀüýûàþÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÓÔÕÖ×ØÙ¶¸¹ºÚ¼¾Û¿'.encode('latin1')
  to_chars =  'abgdezh8iklmn3oprsstufxywaehiiiouuuwABGDEZH8IKLMNJOPRSTYFXCWAEHIIOUUW'.encode('latin1')
  trantab = bytes.maketrans( from_chars, to_chars )
  text = text.translate(trantab)
  return text.decode('utf-8', 'ignore')

        
