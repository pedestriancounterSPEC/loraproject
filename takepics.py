improt RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
i = 0
try:
	while True:
		# need this to take a unique photo name for each picture
		i = i +1
		raspistill -o /home/Desktop/ExploreOpencvDnn-master/images -ex i --nopreview
