import RPi.GPIO as GPIO
import time
from utils import smooth_move
from utils import start

right = 20
left = 0

base_pos = 100 
shoulder_pos = 90 
arm_pos = 90 
wrist_pos = 90 
grasp_pos = 70 

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

base = GPIO.PWM(26, 50) # red connector 4
shoulder = GPIO.PWM(12, 50) #blue connector 2 
arm = GPIO.PWM(21, 50) # orange 
wrist = GPIO.PWM(16, 50) # green connector 5 
grasp = GPIO.PWM(20, 50) # green connector 6 

#start(base, base_pos,"Base" )
#start(shoulder, shoulder_pos,"Shoulder" )
#start(arm, arm_pos,"Arm" )
#start(wrist, wrist_pos,"Wrist" )

start(grasp, grasp_pos,"Grasp" )
time.sleep(5)

#smooth_move(base, base_pos, base_pos + 90, "Base")
#smooth_move(shoulder, shoulder_pos, shoulder_pos + 90, "Shoulder")
#smooth_move(arm, arm_pos, arm_pos + right, "Arm")
#smooth_move(wrist, wrist_pos, wrist_pos + right, "Wrist")

smooth_move(grasp, grasp_pos, grasp_pos + right, "Grasp")
time.sleep(50)

#smooth_move(shoulder, shoulder_pos + right, shoulder_pos-left, "Shoulder")
#smooth_move(arm, arm_pos + right, arm_pos - left, "Arm")
#smooth_move(wrist, wrist_pos + right, wrist_pos - left, "Wrist")
smooth_move(grasp, grasp_pos + right, grasp_pos - left, "Grasp")
time.sleep(5)
#smooth_move(arm, arm_pos - left, arm_pos, "Arm")
#smooth_move(wrist, wrist_pos - left, wrist_pos, "Wrist")
smooth_move(grasp, grasp_pos - left, grasp_pos, "Grasp")
time.sleep(5)

# base.stop()
# shoulder.stop()
# arm.stop()
# wrist.stop()
grasp.stop()
