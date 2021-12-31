import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO_PIN=4
GPIO.setup(GPIO_PIN,GPIO.OUT)

frequency = 400 # hertz
c = 261
d = 294
e = 329
f = 349
g = 392
a = 440
h = 493

try:
	#while True:
	#GPIO.output(buzzer,GPIO.HIGH)
	#time.sleep(0.5)
	#GPIO.output(buzzer,GPIO.LOW)
	#time.sleep(0.5)

	pwm = GPIO.PWM(GPIO_PIN, frequency)
	pwm.start(50)
	time.sleep(0.5)
	pwm.ChangeFrequency(e)
	time.sleep(0.5)
	pwm.ChangeFrequency(e)
	time.sleep(0.5)
	pwm.ChangeFrequency(g)
	time.sleep(0.5)
	pwm.ChangeFrequency(h)
	time.sleep(0.5)
	pwm.ChangeFrequency(h)
except KeyboardInterrupt:
        GPIO.cleanup()
        pass