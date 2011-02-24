from time import sleep
from threading import Thread
from socket import error as SocketError
from mpd import MPDClient, ConnectionError
from config_mod import HOSTS , PORT
SONG=""
class get_mpd(Thread):
  def run (self):
    global HOSTS,PORT,CON_ID,SONG 
    host=HOSTS[0]
    client=MPDClient()
    while True:
      CON_ID = {'host':host, 'port':PORT}
      try:  
        client.connect(**CON_ID)
        SONG=' ^i(/home/master/.icons/dzen2/music.xbm)'+str(client.currentsong()['artist'])+" - "+str(client.currentsong()['title'])
        sleep(1)
      except ConnectionError:
        SONG=' ^i(/home/master/.icons/dzen2/music.xbm)'+str(client.currentsong()['artist'])+" - "+str(client.currentsong()['title'])
        sleep(1)
      except SocketError:
        host=HOSTS[1]
        continue
