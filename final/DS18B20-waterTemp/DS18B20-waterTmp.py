#!/usr/bin/env python

import os
import redis
from time import sleep
#from daemonize import Daemonize

confDoc = open('/home/pi/sensors/final/DS18B20-waterTemp/config.txt','r')
NameS = confDoc.readline().rstrip()
path = confDoc.readline().rstrip()
updateRate = int(confDoc.readline())
redisName = confDoc.readline().rstrip()

DB = redis.StrictRedis(host=redisName, port=6379, db=0)
# pid = "/tmp/water_temp.pid"
r = 0

def main():
	global r
	while True:
		r += 1
		f = open(path, "r")
		data = f.read()
		f.close()

		(discard, sep, reading) = data.partition(' t=')

		temperature = float(reading) / 1000.0
		DB.set(NameS, str(temperature))
		sleep(updateRate)
main()
#daemon = Daemonize(app="waterTemp_sensor", pid=pid, action=main)
#daemon.start()