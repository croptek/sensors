from __future__ import division
import RPi.GPIO as GPIO  
import time     # this lets us have a time delay (see line 12)    

flow = 0
p = 0
pCumulative = 0
t = .3
pin = 27
sConst = 3550

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(pin, GPIO.IN)    # set GPIO25 as input (button)

def pulse(channel):
	global p 
	p += 1

GPIO.add_event_detect(pin, GPIO.RISING, callback=pulse)

while True:
	pCumulative = pCumulative + p
	flow = p/t/sConst*60
	volume = pCumulative/sConst
	p = 0
	print "Pulse rate: ", pCumulative
	print "Flow :", flow, "l/min"
	print "Volume :", volume, "l"  
	time.sleep(t)
