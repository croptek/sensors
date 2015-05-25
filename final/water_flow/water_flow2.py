#!/usr/bin/env python
from __future__ import division
import RPi.GPIO as GPIO  
from time import sleep
#from daemonize import Daemonize    # this lets us have a time delay (see line 12)    
import redis

confDoc = open('/home/pi/sensors/final/water_flow/config.txt','r')
NameS0 = confDoc.readline().rstrip()
NameS1 = confDoc.readline().rstrip()
pinS0 = int(confDoc.readline())
pinS1 = int(confDoc.readline())
updateRate = float(confDoc.readline())
redisName = confDoc.readline().rstrip()

DB = redis.StrictRedis(host=redisName, port=6379, db=0)
pid = "/tmp/water_flow.pid"
flow0 = 0
flow1 = 0
p0 = 0
p1 = 0
p0Cumulative = 0
p1Cumulative = 0
sConst = 3550

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(pinS0, GPIO.IN)    # set GPIO25 as input (button)
GPIO.setup(pinS1, GPIO.IN)    # set GPIO25 as input (button)

def pulse0(channel):
	global p0 
	p0 += 1

def pulse1(channel):
	global p1 
	p1 += 1

GPIO.add_event_detect(pinS0, GPIO.RISING, callback=pulse0)
GPIO.add_event_detect(pinS1, GPIO.RISING, callback=pulse1)

def main():
	global p0, p1
	while True:
		flow0 = p0/updateRate/sConst*60
		flow1 = p1/updateRate/sConst*60

		DB.set(NameS0, str(flow0))
		DB.set(NameS1, str(flow1))
		
		p0 = 0
		p1 = 0 
		
		sleep(updateRate)

main()
#daemon = Daemonize(app="flow_sensor", pid=pid, action=main)
#daemon.start()
