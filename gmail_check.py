from time import sleep
from threading import Thread
from config_mod import GMAIL_BACKGROUND_COLOR,GMAIL_COLOR,GMAIL_UNREAD_COLOR,GMAIL_USERNAME,GMAIL_PASSWORD,ICON_PATH
from colors import *
import imaplib
UNREAD=" NoConnection"
class gmail(Thread):
  def run(self):
    global UNREAD
    while True:
      try:
        srv = imaplib.IMAP4_SSL("imap.gmail.com")
        count=[]
        srv.login(GMAIL_USERNAME,GMAIL_PASSWORD)
        srv.select()
        status,count=srv.search(None,'UnSeen')
      #unseen= len(c.get_inbox_conversations(is_unread=True))
        UNREAD=" "+set_colors(GMAIL_UNREAD_COLOR,GMAIL_BACKGROUND_COLOR)+str(len(count[0][1:].split()))+set_colors(GMAIL_COLOR,GMAIL_BACKGROUND_COLOR)+" ^i("+ICON_PATH+"/envelope.xbm)"+set_normal_color()
        srv.close()
        srv.logout()
        sleep(60)
      except:
        sleep(60)

