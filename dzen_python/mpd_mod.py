from time import sleep
from threading import Thread
from socket import error as SocketError
from mpd import MPDClient, ConnectionError
from config_mod import HOSTS , PORT
SONG=""

def song():
    return SONG
class get_mpd(Thread):
    def run (self):
        global HOSTS,PORT,CON_ID,SONG 
        current_host = 0
        client=MPDClient()
        while True:
            host=HOSTS[current_host]
            CON_ID = {'host':host, 'port':PORT}
            sleep(3)
            try:  
                client.connect(**CON_ID)
                SONG='^i(/home/master/.icons/dzen2/music.xbm) '+str(client.currentsong()['artist'])+" - "+str(client.currentsong()['title'])
                client.disconnect()
                continue
            except ConnectionError: 
                continue
            except:
                SONG='^i(/home/master/.icons/dzen2/music.xbm) '+'n/a'
                continue
