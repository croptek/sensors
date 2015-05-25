#!/bin/sh
 
sudo apt-get update
sudo apt-get install python-smbus -y
sudo apt-get install i2c-tools -y

sudo echo "i2c-bcm2708 
i2c-dev 
w1-gpio 
w1_therm" >> /etc/modules 
sudo echo "dtparam=i2c1=on 
dtparam=spi=on 
dtoverlay=w1-gpio" >> /boot/config.txt 

sudo apt-get install python3-pip -y
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get update
sudo apt-get install build-essential python-dev -y
sudo python setup.py install
sudo apt-get install ntpdate -y 

sudo reboot
#test I2C: sudo i2cdetect -y 1
#test SPI: wget https://raw.githubusercontent.com/raspberrypi/linux/rpi-3.10.y/
#Documentation/spi/spidev_test.c
#				 gcc -o out.o spidev_test1.c
#				 out.o -D /dev/spidev0.0