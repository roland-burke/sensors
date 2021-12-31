import RPi.GPIO as GPIO
import time

# setup led module
GPIO.setmode(GPIO.BCM)
green = 27
red = 17
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)
 
ObstaclePin = 4
 
def setup():
	GPIO.setmode(GPIO.BCM) # Set GPIO by numbers
	GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
def loop():
	print("Obstacle Avoidance Sensor Test \n")
	while True:
		if (GPIO.input(ObstaclePin) == 0):
			RED.start(100)
			GREEN.start(0)
			time.sleep(0.8)
			#print("DETECTED: There is an obstacle ahead")
		else:
			RED.start(0)
			GREEN.start(100)
			#print("Nothing")
 
def destroy():
	GPIO.cleanup() # Release resource
 
if __name__ == '__main__': # The Program start here
	setup()
try:
	loop()
except KeyboardInterrupt: # Control C is pressed, the child program destroy will be executed.
	destroy()