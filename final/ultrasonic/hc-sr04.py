import RPi.GPIO as GPIO
from time import sleep
from daemonize import Daemonize    # this lets us have a time delay (see line 12)    
import redis

confDoc = open('/home/pi/sensors/final/water_flow/config.txt','r')
NameS = confDoc.readline().rstrip()
TRIG = int(confDoc.readline())
ECHO = int(confDoc.readline())
updateRate = float(confDoc.readline())
redisName = confDoc.readline().rstrip()

DB = redis.StrictRedis(host=redisName, port=6379, db=0)
pid = "/tmp/range.pid"

GPIO.setmode(GPIO.BCM)  
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

if(updateRate < 2):
    updateRate = 2

def main():
    while True: 
        GPIO.output(TRIG, False)
        sleep(2) #Waiting For Sensor To Settle
         
        GPIO.output(TRIG, True)
        sleep(0.00001)
        GPIO.output(TRIG, False)
         
        while GPIO.input(ECHO)==0:
          pulse_start = time.time()
         
        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        sleep(updateRate-2)

daemon = Daemonize(app="flow_sensor", pid=pid, action=main)
daemon.start()