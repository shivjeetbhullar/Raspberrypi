import RPi.GPIO as GPIO
from functions import motion_detect
import time
from fc2 import face_dete

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motion_pin,motor_pin,red_pin = 17,27,26

GPIO.setup(motion_pin, GPIO.IN)
GPIO.setup(red_pin, GPIO.OUT)

GPIO.setup(motor_pin, GPIO.OUT)
motor=GPIO.PWM(motor_pin,50)
GPIO.output(red_pin,GPIO.HIGH)

print('Starting Motion Detector')
while True:
	 if motion_detect(motion_pin):
		 time.sleep(0.2)
		 if face_dete():
			 GPIO.cleanup(red_pin)
			 motor.start(5)
			 time.sleep(0.2)
			 motor.ChangeDutyCycle(12.5)
			 time.sleep(0.2)
			 print('Door Unlocked')
			 for x in reversed(range(10)):
				 print('Door Is Closing Again in ',x,' seconds')
				 time.sleep(1)
			 motor.ChangeDutyCycle(5)
			 
			 exit()
	 
	 
	 
#except KeyboardInterrupt:GPIO.cleanup();exit()

GPIO.cleanup()
