import adafruit_dht
import board
import time
import curses

dht_device = adafruit_dht.DHT11(board.D4)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

while(True):
	
	try:
		temperature = dht_device.temperature
		humidity = dht_device.humidity

		stdscr.clrtoeol()
		stdscr.refresh()

		stdscr.addstr(0, 0, "Humiditiy Range: 20 - 90%")
		stdscr.addstr(1, 0, "Temperature Range: 0 - 50°C")
		stdscr.addstr(2, 0, "===========================")

		stdscr.addstr(3, 0, "Temperatur: {:.1f} °C".format(temperature))
		stdscr.addstr(4, 0, "Luftfeuchtigkeit: {} %".format(humidity))

	except:
		stdscr.addstr(0, 0, "Humiditiy Range: 20 - 90%")
		stdscr.addstr(1, 0, "Temperature Range: 0 - 50°C")
		stdscr.addstr(2, 0, "===========================")
		stdscr.addstr(3, 0, "")
		stdscr.addstr(4, 0, "Sensor read failed, trying again..")

	time.sleep(1)
