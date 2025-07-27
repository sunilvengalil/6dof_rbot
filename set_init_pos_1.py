import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

shoulder_pos = 140
arm_pos = 195
arm_dest = 180
shoulder_pos = 10
wrist_pos = 90
wrist_dest = 70


grasp_pos = 181 
grasp_dest = 130 

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

wrist_rot = GPIO.PWM(13, 50) # white 
elbow = GPIO.PWM(21, 50)# orange
grasp = GPIO.PWM(20, 50) # black
wrist = GPIO.PWM(16, 50) #green
shoulder = GPIO.PWM(12, 50) #red
base = GPIO.PWM(26, 50) # yellow

start(base, base_pos,"Base" )
start(arm, arm_pos, "Arm")
start(shoulder, shoulder_pos,"Shoulder")
start(wrist_rot, wrist_pos, "Wrist")
start(grasp, grasp_pos, "Grasp")

smooth_move(arm, arm_pos, arm_dest, "Arm")
#smooth_move(grasp, grasp_pos, grasp_dest, "Grasp",20)
time.sleep(4)
#smooth_move(grasp, grasp_dest, grasp_pos, "Grasp",20)
smooth_move(arm, arm_dest, arm_pos,"Arm")
time.sleep(4)

#base.stop()
#arm.stop()
exit(0)
