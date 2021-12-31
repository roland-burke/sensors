import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO_PIN=4
GPIO.setup(GPIO_PIN,GPIO.OUT)

try:
	while True:
		GPIO.output(GPIO_PIN,GPIO.HIGH)
		time.sleep(5)
		GPIO.output(GPIO_PIN,GPIO.LOW)
		time.sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
        pass