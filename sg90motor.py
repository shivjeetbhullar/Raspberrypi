import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

theta = [x+1 for x in range(5)]
r = np.sin(theta)

fig = plt.figure()

fig.set_facecolor('tab:blue')

ax = fig.add_subplot(111, polar=True)
ax.set_autoscale_on(True)
ax.set_facecolor('tab:blue')

c = ax.scatter(theta, ['10cm','30cm','60cm','90cm','100cm'], c=r, s=30, cmap='hsv', alpha=1)
x = [x for x in range(5)]

line, = ax.plot([1,1,1,1,1],[0,1,2,3,4],color='red')
ax.set_thetamin(0)
ax.set_thetamax(180)
control = [0.1,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14]
#exit()
servo = 2
GPIO_TRIGGER = 20
GPIO_ECHO = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(servo,GPIO.OUT)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

p=GPIO.PWM(servo,50)# 50hz frequency

p.start(0.1)# starting duty cycle ( it set the servo to 0 degree )

n,forw=0.1,True

try:
       while True:
           for x in control:
             p.ChangeDutyCycle(x)
             time.sleep(0.20)
             dist = distance()
             print("Measured Distance = %.1f cm" % dist)
             
           
           for x in control[::-1]:
             p.ChangeDutyCycle(x)
             time.sleep(0.20)
             dist = distance()
             print("Measured Distance = %.1f cm" % dist)
           
except KeyboardInterrupt:
    GPIO.cleanup()
    
