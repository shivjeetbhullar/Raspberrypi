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

c = ax.scatter(theta, ['0cm','5cm','10cm','15cm','20cm'], c=['green','green','blue','red','pink'], s=90, cmap='hsv', alpha=1)
x = [x for x in range(5)]

line, = ax.plot([1,1,1,1,1],[0,1,2,3,4],color='red')
ax.set_thetamin(0)
ax.set_thetamax(180)
control = [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14]
#exit()
servo = 2
GPIO_TRIGGER = 20
GPIO_ECHO = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(servo,GPIO.OUT)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance

p=GPIO.PWM(servo,50)
p.start(0.5)
time.sleep(4)

n,forw,objectsx,objectsy,objectscol=0.1,True,[],[],[]

def updategraph(distance):
    global n,forw,objectsx,objectsy,objectscol,c,ax,plt
    if forw:n+=0.1
    else:n=n-0.1
    if distance < 10:col,locy = 'red',1
    elif distance < 15:col,locy = 'yellow',2
    elif distance > 20 and distance < 35:col,locy = 'pink',3
    else:locy,col=0,'green'
    #else:col,locy='green',1
    objectsx.append(n);objectsy.append(locy);objectscol.append(col)
    
    c.set_offsets(np.c_[objectsx,objectsy])
    c.set_color(objectscol)
    if n >= 3:
        forw,objectsx,objectsy,objectscol= False,[],[],[]
    elif n < 0 and not forw:
        forw,objectsx,objectsy,objectscol= True,[],[],[]
    line.set_xdata([n for x in range(5)])
    ax.relim()
    plt.draw()
    plt.pause(0.20)

try:
       while True:
           for x in control:
             p.ChangeDutyCycle(x)
             dist = distance()
             updategraph(dist)
             print("Measured Distance = %.1f cm" % dist)
             
           
           for x in control[::-1]:
             p.ChangeDutyCycle(x)
             dist = distance()
             updategraph(dist)
             print("Measured Distance = %.1f cm" % dist)
           
except KeyboardInterrupt:
    GPIO.cleanup()
    
