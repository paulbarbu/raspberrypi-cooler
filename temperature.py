#! /usr/bin/python2.7

import RPi.GPIO as GPIO
import sys
import subprocess
from datetime import datetime

FAN = 7
MAX_TEMP = 55

def sendmail(subject, body):
	subprocess.call('~/localhost/sendmail.sh "{0}" "{1}"'.format(subject, body), shell=True)


def confGPIO():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(FAN, GPIO.OUT, initial=GPIO.HIGH)


def startFan():
	print str(datetime.now()) + ' Starting fan'
	#sendmail('[fan] start!', 'Temp is {0} - starting fan!'.format(getTemp()))
	GPIO.output(FAN, GPIO.HIGH)


def stopFan():
	print str(datetime.now()) + ' Stopping fan'
	GPIO.output(FAN, GPIO.LOW)
	# this should be done only here in order to allow the fan to keep running when the script exists
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
		print str(datetime.now()) + ' CPU Temperature: ' + str(t) + ' MAX temp: ' + str(MAX_TEMP)
		if t >= MAX_TEMP:
			startFan()
		else:
			stopFan()



if '__main__'== __name__:
	main()
