import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

shoulder_pos = 140
arm_pos = 195
wrist_rot_pos = 90
wrist_pos = 10
grasp_pos = 181 
base_pos = 90 


grasp_dest = 130 
shoulder_dest = 100 
arm_dest = 180
wrist_dest = 70

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

wrist_rot = GPIO.PWM(13, 50) # brown 
arm = GPIO.PWM(21, 50) # orange
grasp = GPIO.PWM(20, 50) # yellow
wrist = GPIO.PWM(16, 50) # green
shoulder = GPIO.PWM(12, 50) # blue
base = GPIO.PWM(26, 50) # red

#start(base, base_pos,"Base" )
start(shoulder, shoulder_pos,"Shoulder")
#start(arm, arm_pos, "Arm")
#start(wrist_rot, wrist_rot_pos, "Wrist")
start(wrist, wrist_pos, "Wrist")
#start(grasp, grasp_pos, "Grasp")

smooth_move(shoulder, shoulder_pos, shoulder_dest, "Shoulder")
#smooth_move(arm, arm_pos, arm_dest, "Arm")
#smooth_move(wrist, wrist_pos, wrist_dest, "Wrist")
#smooth_move(grasp, grasp_pos, grasp_dest, "Grasp",20)
time.sleep(10)
smooth_move(shoulder, shoulder_dest, shoulder_pos, "Shoulder")
#smooth_move(wrist, wrist_dest, wrist_pos, "Wrist")
#smooth_move(grasp, grasp_dest, grasp_pos, "Grasp",20)
#smooth_move(arm, arm_dest, arm_pos,"Arm")
time.sleep(10)

#base.stop()
#arm.stop()
exit(0)
