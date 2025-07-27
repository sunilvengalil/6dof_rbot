import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

right = 30
left = 30
base_pos = 90 
shoulder_pos = 90 

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

base = GPIO.PWM(26, 50) # red
shoulder = GPIO.PWM(12, 50) #blue 

#start(base, base_pos,"Base" )
start(shoulder, shoulder_pos,"Shoulder" )

#smooth_move(base, base_pos, base_pos + 90, "Base")
smooth_move(shoulder, shoulder_pos, shoulder_pos + right, "Shoulder")
time.sleep(5)
smooth_move(shoulder, shoulder_pos + right, shoulder_pos -  left, "Shoulder")
time.sleep(5)
smooth_move(shoulder, shoulder_pos -  left, shoulder_pos, "Shoulder")
time.sleep(5)

base.stop()
shoulder.stop()
