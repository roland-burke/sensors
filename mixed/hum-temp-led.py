import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import curses

# setup DHT11 humidity and temperature sensor
dht_device = adafruit_dht.DHT11(board.D4)

# setup print for sensor data
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

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

# general setup
RUNNING = True
maxTemp = 30

def power_led(value):
	if value > 100:
		value = 100
	RED.start(value)
	GREEN.start(0)
	BLUE.start(100 - value)

def get_percentage(absoluteTemp):
	return absoluteTemp / maxTemp * 100

# test led
for i in range(maxTemp):
	time.sleep(0.1)
	power_led(get_percentage(i))

try:
	while(RUNNING):

		try:
			temperature = dht_device.temperature
			humidity = dht_device.humidity

			power_led(get_percentage(temperature))

			stdscr.clrtoeol()
			stdscr.refresh()

			stdscr.addstr(0, 0, "Humiditiy Range: 20 - 90%")
			stdscr.addstr(1, 0, "Temperature Range: 0 - 50°C")
			stdscr.addstr(2, 0, "===========================")

			stdscr.addstr(3, 0, "Temperatur: {:.1f} °C".format(temperature))
			stdscr.addstr(4, 0, "Luftfeuchtigkeit: {} %".format(humidity))

		except RuntimeError:
			stdscr.addstr(0, 0, "Humiditiy Range: 20 - 90%")
			stdscr.addstr(1, 0, "Temperature Range: 0 - 50°C")
			stdscr.addstr(2, 0, "===========================")
			stdscr.addstr(3, 0, "")
			stdscr.addstr(4, 0, "Sensor read failed, trying again..")

		time.sleep(1)
except KeyboardInterrupt:
	#the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
	curses.echo()
	curses.nocbreak()
	curses.endwin()
	RUNNING = False
	GPIO.cleanup()