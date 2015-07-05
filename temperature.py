#! /usr/bin/python2.7

import RPi.GPIO as GPIO
import sys

FAN = 7
MAX_TEMP = 55 

def confGPIO():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(FAN, GPIO.OUT, initial=GPIO.HIGH)


def startFan():
	print 'Starting fan'
	GPIO.output(FAN, GPIO.HIGH)


def stopFan():
	print 'Stopping fan'
	GPIO.output(FAN, GPIO.LOW)
	GPIO.cleanup()


def getTemp():
	t = -1
	with open('/sys/class/thermal/thermal_zone0/temp') as f:
		try:
			t = float(f.read())/1000;
		except ValueError:
			t = -1
	return t
		

def main():
	confGPIO()

	if 'start' in sys.argv:
		startFan()
	elif 'stop' in sys.argv:
		stopFan()
	else:
		t = getTemp() 
		print 'CPU Temperature: ' + str(t) + ' MAX temp: ' + str(MAX_TEMP)
		if t >= MAX_TEMP:
			startFan()
		else:
			stopFan()


if '__main__'== __name__:
	main()
