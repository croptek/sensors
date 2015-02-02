
import time
import smbus

from smbus import SMBus
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
	return

def main():
	enable()
	while True:
		Light()
		time.sleep(3)
if __name__ == "__main__":
	main()
