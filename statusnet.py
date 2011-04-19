from time import sleep
import threading
import re
import urllib2
from config_mod import STATUSNET_URL, STATUSNET_USER_COLOR, STATUNET_BACKGROUND_COLOR
from colors import *
STATUSNET=""

class get_statusnet(threading,Thread):
	def run( self ):
		global STATUSNET

		while True:
			try:
				status = simplejson.load(urllib2.urlopen(STATUSNET_URL))
				for i in range(0,2):
					status_user = ' '+set_colors(STATUSNET_USER_COLOR,STATUSNET_BACKGROUND_COLOR)+status[i]['user']
					text = status[i]['text']
					for j in range(0,len(text))
						status_text = ' '+set_colors(STATUSNET_COLOR,STATUSNET_BACKGROUND_COLOR)+text[i:]
						STATUSNET = status_user + status_text
						sleep(100)
				continue		
			except (urlibb2.URLError):
				STATUSNET=' '+setcolors(STATUSNET_COLOR,STATUSNET_BACKGROUND_COLOR)+"Cannot connect"+set_normal_color()
				sleep(60)
				
