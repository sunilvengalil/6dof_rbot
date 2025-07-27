import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

right = 40
left = 40

base_pos = 90 
shoulder_pos = 90 
arm_pos = 90 

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

base = GPIO.PWM(26, 50) # red
shoulder = GPIO.PWM(12, 50) #blue 
arm = GPIO.PWM(21, 50) # orange 

#start(base, base_pos,"Base" )
#start(shoulder, shoulder_pos,"Shoulder" )
start(arm, arm_pos,"Arm" )
time.sleep(5)
#smooth_move(base, base_pos, base_pos + 90, "Base")
#smooth_move(shoulder, shoulder_pos, shoulder_pos + 90, "Shoulder")
smooth_move(arm, arm_pos, arm_pos + right, "Arm")
time.sleep(5)
#smooth_move(shoulder, shoulder_pos + right, shoulder_pos-left, "Shoulder")
smooth_move(arm, arm_pos + right, arm_pos - left, "Arm")
time.sleep(5)
smooth_move(arm, arm_pos - left, arm_pos, "Arm")
time.sleep(5)

# base.stop()
# shoulder.stop()
arm.stop()
