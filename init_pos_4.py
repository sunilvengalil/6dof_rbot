import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

right = 20
left = 20
arm_right = 20
arm_left = 0

grasp_right = 10
grasp_left = 10

base_pos = 90 
shoulder_pos = 140 
arm_pos = 20 
wrist_pos = 160 
wrist_rot_pos = 90 
grasp_pos = 90 

wrist_dest =90 
arm_dest = 90
shoulder_dest = 90
base_dest = 20

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

start(base, base_pos, "Base" )
start(shoulder, shoulder_pos, "Shoulder" )
start(arm, arm_pos, "Arm" )
start(wrist, wrist_pos, "Wrist" )
start(wrist_rot, wrist_rot_pos, "Wrist rotation" )
start(grasp, grasp_pos, "Grasp" )
time.sleep(3)

smooth_move(arm, arm_pos, arm_pos + arm_right, "Arm")
#smooth_move(base, base_pos, base_pos + right, "Base")
#smooth_move(arm, arm_pos, arm_dest, "Arm")
#smooth_move(wrist_rot, wrist_rot_pos, wrist_rot_pos + right, "Wrist Rotation")
smooth_move(grasp, grasp_pos, grasp_pos + grasp_right, "Grasp")

time.sleep(5)

smooth_move(grasp, grasp_pos + grasp_right, grasp_pos - grasp_left, "Grasp")
#smooth_move(wrist_rot, wrist_rot_pos+right, wrist_rot_pos - left, "Wrist Rotation")
#smooth_move( base,  base_pos + right, base_pos-left, "Base")
smooth_move(arm, arm_pos + arm_right, arm_pos - arm_left, "Arm")
#smooth_move(wrist_rot, wrist_rot_pos + right, wrist_rot_pos - left, "Wrist Rotation")
#smooth_move(wrist, wrist_dest, wrist_pos, "Wrist")
#smooth_move(arm, arm_pos+arm_right, arm_pos, "Arm")
#smooth_move(shoulder, shoulder_dest, shoulder_pos, "Shoulder")

time.sleep(3)

#smooth_move(wrist_rot, wrist_rot_pos-left, wrist_rot_pos , "Wrist Rotation")
#smooth_move(base, base_pos - left, base_pos, "Base")
smooth_move(grasp, grasp_pos - grasp_left, grasp_pos, "Grasp")
smooth_move(arm, arm_pos - arm_left, arm_pos , "Arm")
#smooth_move(wrist, wrist_pos - left, wrist_pos, "Wrist")

time.sleep(5)

print("Exiting...")

base.stop()
shoulder.stop()
arm.stop()
wrist.stop()
wrist_rot.stop()
grasp.stop()
