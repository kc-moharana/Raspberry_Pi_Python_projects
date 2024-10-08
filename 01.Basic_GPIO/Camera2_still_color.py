'''
Take a picture
'''

import os, re, sys
from datetime import datetime
from time import sleep
from signal import pause
from picamzero import Camera

cam = Camera()
cam.start_preview()
sleep(2)
pic = os.path.join('/home/pi/Pictures', f'cam_{datetime.now():%Y-%m-%d-%H-%M-%S}.jpg')
cam.take_photo(pic)
print(f'Photo saved to : {pic}')