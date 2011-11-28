#!/usr/bin/env python
from threading import Thread
from config_mod import TF_USER,TF_PASS,TF_ADD
from time import sleep
import urllib, urllib2, cookielib, BeautifulSoup

username = TF_USER
password = TF_PASS
address=TF_ADD
D_SPEED=''
U_SPEED=''
SPEEDS=''
class get_tflux(Thread):
  def run(self):
    global D_SPEED,U_SPEED,SPEEDS
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'username' : username, 'iamhim' : password})
    opener.open('http://'+address+'/login.php', login_data)
    #print resp.readlines()
    while 1:
      resp = opener.open('http://'+address+'/index.php?iid=index')
      mytext=''.join(BeautifulSoup.BeautifulSoup(resp).findAll(text=True))
      mytext=mytext.split()
      for i in range(len(mytext)):
        if mytext[i]=="Download":
          D_SPEED=mytext[i+2][:len(mytext[i+2])-3]+mytext[i+3][0]
          break
      for i in range(len(mytext)):
        if mytext[i]=="Upload" and mytext[i+1]=='Speed:':
          U_SPEED=mytext[i+2][:len(mytext[i+2])-3]+mytext[i+3][0]
          break
      SPEEDS=' D '+D_SPEED+' U '+U_SPEED
      sleep(1)
