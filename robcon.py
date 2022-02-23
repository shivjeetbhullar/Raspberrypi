from RPi import GPIO
from time import sleep
import getch

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

mode = 'N'


def runstraight():
    global mode
    GPIO.output(m1p1,GPIO.HIGH)
    GPIO.output(m1p2,GPIO.LOW)
    GPIO.output(m2p1,GPIO.HIGH)
    GPIO.output(m2p2,GPIO.LOW)
    m1.ChangeDutyCycle(80)
    m2.ChangeDutyCycle(80)
    mode = 'S'
    print('Moving Forward')

def reverse():
    GPIO.output(m1p1,GPIO.LOW)
    GPIO.output(m1p2,GPIO.HIGH)
    GPIO.output(m2p1,GPIO.LOW)
    GPIO.output(m2p2,GPIO.HIGH)
    m1.ChangeDutyCycle(80)
    m2.ChangeDutyCycle(80)
    mode = 'B'

def moveright():
    global mode
    m2.ChangeDutyCycle(0)
    m1.ChangeDutyCycle(60)
    mode = 'R'
    print('Moving Right')


def moveleft():
    global mode
    m1.ChangeDutyCycle(0)
    m2.ChangeDutyCycle(60)
    mode = 'L'
    print('Moving Left')
    
def stop():
    m1.ChangeDutyCycle(0)
    m2.ChangeDutyCycle(0)
    
try:
    m1.start(80)
    m2.start(80)
    while True:
        val = getch.getche()
        if val=='a':
            moveright()
        elif val=='d':
            moveleft()
        elif val=='w':
            runstraight()
        elif val=='s':
            reverse()
        else:
            stop()
        
except:
    GPIO.cleanup()
