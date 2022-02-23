import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)

trig,echo,buzz,safe_led = 17,27,22,26
buzz_s = False
print('Distance MEasurement In Progress')
gp.setup(trig,gp.OUT)


def do_safe():
	gp.setup(safe_led,gp.OUT)
	gp.output(safe_led,gp.HIGH)
	

def do_beep(distance):
	global buzz_s
	gp.setup(21,gp.OUT)
	gp.setup(buzz,gp.OUT)
	buzz_s = not buzz_s
	gp.output(buzz,buzz_s) 
	gp.output(21,buzz_s) 
	time.sleep(distance/180)
	
	gp.cleanup(buzz);gp.cleanup(21)
	
	
gp.setup(echo,gp.IN)
gp.output(trig,False)


print("Waiting For Sensor To Settle")
time.sleep(2)

while True:
	try:
	 gp.output(trig,True)
	 time.sleep(0.1)
	 gp.output(trig,False)
	 while gp.input(echo) == 0:
	  pulse_start = time.time()
	 while gp.input(echo) == 1:
	  pulse_end = time.time()
	 pulse_dur = pulse_end - pulse_start
	 distance = pulse_dur * 17150
	 distance = round(distance,2)
	 if int(distance) < 20:
		 gp.cleanup(safe_led)
		 do_beep(distance)
		 print('Object Is Close ',distance,"cm")
	 else:
		 do_safe()
		 print("Distance ",distance,"cm")
	except KeyboardInterrupt:gp.cleanup();exit()














