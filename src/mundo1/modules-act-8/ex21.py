import time
from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('./src/modules-act-8/teste.mp3')
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)