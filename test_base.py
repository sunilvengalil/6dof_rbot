import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

right = 20
left = 20
base_pos = 90 

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

base = GPIO.PWM(26, 50) # red
start(base, base_pos,"Base" )

smooth_move(base, base_pos, base_pos + right, "Base")
time.sleep(3)
smooth_move(base, base_pos + right, base_pos-left, "Base")
time.sleep(3)
smooth_move(base, base_pos - left, base_pos, "Base")
time.sleep(3)

base.stop()
