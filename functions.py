import RPi.GPIO as GPIO
import time

def motion_detect(motion_pin):
	if GPIO.input(motion_pin):
		return True
	else:print("No Motin")
	time.sleep(0.5)
