import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

right = 0
left = 10

base_pos = 90 
shoulder_pos = 90 
arm_pos = 0 
wrist_pos = 160 
wrist_rot_pos = 90 
grasp_pos = 90 

wrist_dest =160 
arm_dest = 30
shoulder_dest = 100 

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

base = GPIO.PWM(26, 50) # red connector 4
shoulder = GPIO.PWM(12, 50) #blue connector 2 
arm = GPIO.PWM(21, 50) # orange connector 3 
wrist = GPIO.PWM(16, 50) # green connector 5 
wrist_rot = GPIO.PWM(13, 50) # brown connector 1 
grasp = GPIO.PWM(20, 50) #  connector 6 

start(base, base_pos,"Base" )
start(shoulder, shoulder_pos,"Shoulder" )
start(arm, arm_pos,"Arm" )
start(wrist, wrist_pos,"Wrist" )
start(wrist_rot, wrist_pos,"Wrist" )
start(grasp, grasp_pos,"Grasp" )
time.sleep(5)
#smooth_move(base, base_pos, base_pos + 90, "Base")
smooth_move(shoulder, shoulder_pos, shoulder_dest, "Shoulder")
smooth_move(arm, arm_pos, arm_dest, "Arm")
smooth_move(wrist, wrist_pos, wrist_dest, "Wrist")
#smooth_move(grasp, grasp_pos, grasp_pos + right, "Grasp")
time.sleep(5)
#smooth_move(shoulder, shoulder_pos + right, shoulder_pos-left, "Shoulder")
smooth_move(wrist, wrist_dest, wrist_pos, "Wrist")
smooth_move(arm, arm_dest, arm_pos, "Arm")
smooth_move(shoulder, shoulder_dest, shoulder_pos, "Shoulder")
#smooth_move(grasp, grasp_pos + right, grasp_pos - left, "Grasp")
time.sleep(3)
#smooth_move(arm, arm_pos - left, arm_pos, "Arm")
#smooth_move(wrist, wrist_pos - left, wrist_pos, "Wrist")
#smooth_move(grasp, grasp_pos - left, grasp_pos, "Grasp")
time.sleep(3)

base.stop()
shoulder.stop()
arm.stop()
wrist.stop()
wrist_rot.stop()
grasp.stop()
