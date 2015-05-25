#!/usr/bin/env python

import time
import smbus
from smbus import SMBus
#import redis
from time import sleep
#from daemonize import Daemonize

confDoc = open('/home/pi/sensors/TSL2561-lux/config.txt','r')
NameS = confDoc.readline().rstrip()
updateRate = float(confDoc.readline())
redisName = confDoc.readline().rstrip()
#pid = "/tmp/lux.pid"

#DB = redis.StrictRedis(host=redisName, port=6379, db=0)

address = 0x39
control_on = 0x03
control_off = 0x00

TSL2561 = SMBus(1)

def enable():
	print "Power ON"
	TSL2561.write_byte(address,0x80) #select command register
	TSL2561.write_byte(address, control_on) #power on

def disable():
	print "Power OFF"
	TSL2561.write_byte(address,0x80) #select command register
	TSL2561.write_byte(address, control_off) #power off	

def Light():
	var = [0, 0, 0, 0]
	var = TSL2561.read_i2c_block_data(0x39, 0x8c)
	chanel0 = ((var[1] << 8) +var[0]) #photodiode 650nm
	chanel1 = ((var[3] << 8) +var[2]) #photodiode 810nm
	print "LIGHT: "+ str(chanel0) + "IR LIGHT:" + str(chanel1)
	return chanel0

def main():
	enable()
	while True:
		lux = Light()
		#DB.set(NameS, str(lux))
		time.sleep(updateRate)

if __name__ == "__main__":
	main()

#daemon = Daemonize(app="lux_sensor", pid=pid, action=main)
#daemon.start()
