#!/usr/bin/env python

import sys
import redis
import Adafruit_DHT
from time import sleep
# from daemonize import Daemonize

confDoc = open('/home/pi/sensors/final/RHT03-tmp&hum/config.txt','r')
tmpSensorName = confDoc.readline().rstrip()
humSensorName = confDoc.readline().rstrip()
pin = int(confDoc.readline())
updateRate = int(confDoc.readline())
redisName = confDoc.readline().rstrip()

# pid = "/tmp/tmp_hum.pid"
DB = redis.StrictRedis(host=redisName, port=6379, db=0)

if updateRate < 2:
	updateRate = 2

def main():
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
		if humidity is not None and temperature is not None:
			DB.set(tmpSensorName, str(temperature))
			DB.set(humSensorName, str(humidity))
		else:
			print 'Failed to get reading. Try again!'
		sleep(updateRate)

# daemon = Daemonize(app="tempHum_sensor", pid=pid, action=main)
# daemon.start()
main()