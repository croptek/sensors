#!/usr/bin/env python

import sys
#import redis
import Adafruit_DHT
import time

confDoc = open('config.txt','r')
sysName = confDoc.readline().rstrip()
tmpSensorName = confDoc.readline().rstrip()
humSensorName = confDoc.readline().rstrip()
pin = int(confDoc.readline())
updateRate = int(confDoc.readline())

redisName = 'localhost'

#print 'Server: '+redisName+', system: '+sysName+', tmp: '+tmpSensorName+', hum: '+humSensorName+', pin: '+str(pin)+', updateRate: '+str(updateRate)

#DB = redis.StrictRedis(host=redisName, port=6379, db=0)
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
if updateRate < 2:
	updateRate = 2

while True:
	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
	# Note that sometimes you won't get a reading and
	# the results will be null (because Linux can't
	# guarantee the timing of calls to read the sensor).  
	# If this happens try again!
	if humidity is not None and temperature is not None:
		#DB.set(sysName+'.Sensors.'+tmpSensorName+'.val', str(temperature))
		#DB.set(sysName+'.Sensors.'+humSensorName+'.val', str(humidity))
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	else:
		print 'Failed to get reading. Try again!'
	time.sleep(updateRate)
