import time
import RPi.GPIO as GPIO

def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = (elapsed * 34300) / 2

    return distance

def measure_safe():
    time.sleep(0.1)
    return measure()

def measure_average():
    distances = [measure_safe() for x in range(5)]
    distance = sum(distances) / len(distances)
    return distance

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 24
GPIO_ECHO = 23

print('Ultrasonic measurement')

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

print("hello")
try:
    while True:
        distance = measure_average()
        print('Distance: %.1f' % distance)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

    
