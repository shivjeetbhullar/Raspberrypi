import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(26,GPIO.LOW)
motor = True

def callback(channel):
        global motor
        #GPIO.cleanup(26)
        if not GPIO.input(channel):
                print("No Water Detected!")
        else:
                print("Water Detected!")
 
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
try:
        while True:
                print(motor)
                #if motor:
                #        GPIO.setup(26,GPIO.OUT)
                 #       GPIO.output(26,GPIO.HIGH)
                time.sleep(1)
except:
        GPIO.cleanup()
