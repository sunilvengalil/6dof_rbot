import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(13, 50)

speedDelay = 20

def smooth_move(p, start, finish):
    if start == finish:
        return
    if start < finish:
        step = 0.05
    else:
        step = -0.05
    num_steps = (int) ((finish - start)/step)

    for j in range(1, num_steps + 1):
        position = start + j * step
        print(position)
        p.changeDutyCycle(position);
        time.sleep(speedDelay/1000);

smooth_move(5,10)
