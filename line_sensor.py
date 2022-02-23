from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

left_sensor = 14
right_sensor = 15

m1p1=22;m1p2=23;m1in = 6
m2p1=20;m2p2=26;m2in = 16

GPIO.setup(m1p1,GPIO.OUT)
GPIO.setup(m1p2,GPIO.OUT)
GPIO.setup(m1in,GPIO.OUT)

GPIO.setup(m2p1,GPIO.OUT)
GPIO.setup(m2p2,GPIO.OUT)
GPIO.setup(m2in,GPIO.OUT)

GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

m1=GPIO.PWM(m1in,1000)
m2=GPIO.PWM(m2in,1000)
m1.start(60)
m2.start(60)

mode = 'N'

def runstraight():
	global mode
	GPIO.output(m1p1,GPIO.HIGH)
	GPIO.output(m1p2,GPIO.LOW)
	GPIO.output(m2p1,GPIO.HIGH)
	GPIO.output(m2p2,GPIO.LOW)
	m1.ChangeDutyCycle(50)
	m2.ChangeDutyCycle(50)
	mode = 'S'


def moveright():
	global mode
	m2.ChangeDutyCycle(0)
	m1.ChangeDutyCycle(40)
	mode = 'R'
	

def moveleft():
	global mode
	m1.ChangeDutyCycle(0)
	m2.ChangeDutyCycle(40)
	mode = 'L'
	

try:
	while True:
		if GPIO.input(left_sensor):
			print("Robot is straying off to the left, move right captain!")
			moveleft()
		elif GPIO.input(right_sensor):
			print("Robot is straying off to the right, move left captain!")			
			moveright()
		else:
			print("Following the line!")
			if not mode=='S':runstraight()
		#sleep(0.2)
except:
	GPIO.cleanup()
