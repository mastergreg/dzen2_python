from time import sleep
from threading import Thread
from alsaaudio import Mixer
VOLUME="N/A" 

def volume():
  return VOLUME
class get_volume(Thread):
  def run (self):
    global VOLUME
    while True:
      VOLUME=str(Mixer('Master').getvolume()[0])
      sleep(1)
