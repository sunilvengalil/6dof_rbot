import RPi.GPIO as GPIO
import time

speedDelay = 30
STEP = 0.01
def move_to(servo, start_pos, name="servo"):
    start_duty_cycle = start_pos / 18 + 2.5
    print(f"Started joint {name} at angle {start_pos}") 
    servo.ChangeDutyCycle(start_duty_cycle)

def start(servo, start_pos, name="servo"):
    start_duty_cycle = start_pos / 18 + 2.5
    print(f"Started joint {name} at angle {start_pos}") 
    servo.start(start_duty_cycle)

def smooth_move(p, start, finish, name, delay=speedDelay):
    if start == finish:
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
    if step > 0 and position < finish_duty_cycle:
        position = finish_duty_cycle 
        p.ChangeDutyCycle(position);
        time.sleep(delay/1000);
    elif step < 0 and position > finish_duty_cycle:
        position = finish_duty_cycle 
        p.ChangeDutyCycle(position);
        time.sleep(delay/1000);
    print(f"Joint {name} reached target position {finish}")

