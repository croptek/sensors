from __future__ import division
import RPi.GPIO as GPIO  
import time     # this lets us have a time delay (see line 12)    

flow = 0
p = 0
t = .3
ct = 1
pin = 25

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(pin, GPIO.IN)    # set GPIO25 as input (button)

def pulse(channel):
	global p 
	p += 1

GPIO.add_event_detect(pin, GPIO.RISING, callback=pulse)

while True:
	flow = p/t/5/450*60
	waterAmount = p/5/450*60
	p = 0
	print flow
	time.sleep(t)
