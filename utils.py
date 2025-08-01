from mqttc.client_sub import get_value, start_mqtt

import RPi.GPIO as GPIO
import time

speedDelay = 30
STEP = 0.01

def grasp(grasp_servo, current_pos):
    print("Staring to grasp")
    if current_pos >= 90:
        print("grasp is already tight. Returning..")
        return
    new_pos = smooth_moove(grasp_servo, current_pos, 90,name="Grasper", max_motor_power=1000)
    return new_pos
   
    
def move_to(servo, start_pos, name="servo"):
    start_duty_cycle = start_pos / 18 + 2.5
    print(f"Started joint {name} at angle {start_pos}") 
    servo.ChangeDutyCycle(start_duty_cycle)

def start(servo, start_pos, name="servo"):
    start_duty_cycle = start_pos / 18 + 2.5
    print(f"Started joint {name} at angle {start_pos}") 
    servo.start(start_duty_cycle)
    return start_pos

def smooth_move(p, start, finish, name, delay=speedDelay, max_motor_power = None):
    if start == finish:
        print("Start and finish are same. Returning")
        return
    if max_motor_power is not None:
        start_mqtt("esp32/grasp_power")
        motor_power = get_value(1000)
        print(f"Motor power before start: {motor_power}")
        if motor_power > max_motor_power:
            print(f" Motor power for {name} is more than maximum {motor_power}. Possible obstacle. Returning..")
            return
    start_duty_cycle = (start / 18) + 2.5
    finish_duty_cycle = (finish / 18) + 2.5
    print(start_duty_cycle, finish_duty_cycle)
    step = STEP
    if start_duty_cycle > finish_duty_cycle:
        step = -step
    num_steps = (int) ((finish_duty_cycle - start_duty_cycle)/step)
    print(f"Moving joint {name} from {start} to {finish}")
    position = start_duty_cycle
    for j in range(1, num_steps + 1):
        position = position + step
        p.ChangeDutyCycle(position);
        time.sleep(delay/1000);
    if step > 0 and position < finish_duty_cycle or (step < 0 and position > finish_duty_cycle):
        position = finish_duty_cycle 
        p.ChangeDutyCycle(position);
        time.sleep(delay/1000);
    print(f"Joint {name} reached target position {finish}")
    return finish

