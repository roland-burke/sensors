import RPi.GPIO as GPIO
import time
 
ObstaclePin = 4
 
def setup():
	GPIO.setmode(GPIO.BCM) # Set GPIO by numbers
	GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
def loop():
	print("Obstacle Avoidance Sensor Test \n")
	while True:
		print("HR: {}".format(GPIO.input(ObstaclePin)))
		time.sleep(0.5)
 
def destroy():
	GPIO.cleanup() # Release resource
 
if __name__ == '__main__': # The Program start here
	setup()
try:
	loop()
except KeyboardInterrupt: # Control C is pressed, the child program destroy will be executed.
	destroy()