
import RPi.GPIO as GPIO     
import time

in1 = 26

GPIO.setmode(GPIO.BCM)



try:
	while True:
		GPIO.setup(in1,GPIO.OUT)
		GPIO.output(26,GPIO.HIGH)
		time.sleep(2)
		GPIO.cleanup(26)
		time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()


#import RPi.GPIO as GPIO
#import time

#control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

#servo = 17

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(servo,GPIO.OUT)
# in servo motor,
# 1ms pulse for 0 degree (LEFT)
# 1.5ms pulse for 90 degree (MIDDLE)
# 2ms pulse for 180 degree (RIGHT)

# so for 50hz, one frequency is 20ms
# duty cycle for 0 degree = (1/20)*100 = 5%
# duty cycle for 90 degree = (1.5/20)*100 = 7.5%
# duty cycle for 180 degree = (2/20)*100 = 10%

#p=GPIO.PWM(servo,50)# 50hz frequency

#p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )


#try:
#	while True:
#		GPIO.output(17,GPIO.HIGH)
#		time.sleep(2)
#		GPIO.output(17,GPIO.LOW)
#except KeyboardInterrupt:
#	GPIO.cleanup()


#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#pin = 15

#GPIO.setup(pin, GPIO.IN)

#print('Starting Motion Detector')
#time.sleep(2)

#try:
 #while True:
	# if GPIO.input(pin):
	#	 print("Motion Detected ",GPIO.input(pin))
	 #else:
		# print("No Motin")
#	 time.sleep(0.5)
	 
	 
#except KeyboardInterrupt:GPIO.cleanup();exit()
#import RPi.GPIO as gp,time
GPIO.cleanup()
#gp.setmode(gp.BCM)

#gp.setup(22,gp.OUT)

#for x in range(10):
 #gp.output(22,gp.HIGH)
 #time.sleep(0.2)
 #print('ff')
 #gp.output(22,gp.LOW)
 #time.sleep(0.2)

#gp.cleanup() 
