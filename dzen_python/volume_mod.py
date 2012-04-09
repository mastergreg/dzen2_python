from time import sleep
from threading import Thread
from alsaaudio import Mixer
VOLUME="N/A" 

def volume():
  return VOLUME
class get_volume(Thread):
  def run (self):
    global VOLUME
    m = Mixer('Master')
    while True:
      VOLUME=str(m.getvolume()[0])
      sleep(5)
