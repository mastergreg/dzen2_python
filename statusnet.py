# -*- coding: utf-8 -*-s
from time import sleep
import simplejson
from threading import Thread
import re
import urllib2
from config_mod import STATUSNET_URL,STATUSNET_COLOR,STATUSNET_USER_COLOR, STATUSNET_BACKGROUND_COLOR
from colors import *
import string
STATUSNET=" "
STATUS=""
class download_url(Thread):
  def run ( self ):
    global STATUS,STATUSNET
    while True:
      try:
        STATUS = simplejson.load(urllib2.urlopen("http://status.foss.ntua.gr/index.php/api/statuses/public_timeline.json?count=3"))
        sleep(60)
      except (urllib2.URLError):
        STATUSNET=' '+set_colors(STATUSNET_COLOR,STATUSNET_BACKGROUND_COLOR)+"Cannot connect"+set_normal_color()
        sleep(60)

class get_statusnet(Thread):
  def run( self ):
    global STATUS,STATUSNET
    download_url().start()
    while True:
      try:
        #			status = simplejson.load(urllib2.urlopen(STATUSNET_URL))
        #			STATUSNET = status[1]['user']['name']
        for i in range(0,3):
          status_user = ' '+set_colors(STATUSNET_COLOR,STATUSNET_BACKGROUND_COLOR)+'StatusNet [' + str(i+1) + '/3]: ' +set_colors(STATUSNET_USER_COLOR,STATUSNET_BACKGROUND_COLOR)+STATUS[i]['user']['screen_name']
          text = STATUS[i]['text']
          text = text.decode('utf-8')
          text = text.encode('iso-8859-7', 'replace')

          from_chars = u'áâãäåæçèéêëìíîïðñóòôõö÷øùÜÝÞßúÀüýûàþÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÓÔÕÖ×ØÙ¶¸¹ºÚ¼¾Û¿'.encode('latin1')
          to_chars =  u'abgdezh8iklmn3oprsstufxywaehiiiouuuwABGDEZH8IKLMNJOPRSTYFXCWAEHIIOUUW'.encode('latin1')
          trantab = string.maketrans( from_chars, to_chars )
          #trantab = dict((ord(a), b) for a, b in zip(from_chars, to_chars))
          text = string.translate( text, trantab )
          #text = text.translate(trantab)
          #text = test
          for j in range(0,len(text),20):
            status_text = ' '+set_colors(STATUSNET_COLOR,STATUSNET_BACKGROUND_COLOR)+text[j:j+25]
            STATUSNET =  status_user + status_text
            sleep(3)
      except:
        sleep(3)
