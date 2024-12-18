import time
import usb_hid
from adafruit_hid.mouse import Mouse
import os

# For LED control
import board
import pwmio

led = pwmio.PWMOut(board.GP22, frequency=5000, duty_cycle=65535)

mouse = Mouse(usb_hid.devices)

wait = os.getenv("MOVE_INTERVAL") / 1000
move_distance = os.getenv("MOVE_STEP")
mouse_moving = os.getenv("MOVE_MOVING")
state = 0

blink_interval = 0.05

print("Mouse mover started")

while mouse_moving:
    if state == 0:
        x, y = move_distance, move_distance
        move_name = "UP_RIGHT"
    elif state == 1:
        x, y = move_distance, -move_distance
        move_name = "DOWN_RIGHT"
    elif state == 2:
        x, y = -move_distance, -move_distance
        move_name = "DOWN_LEFT"
    elif state == 3:
        x, y = -move_distance, move_distance
        move_name = "UP_LEFT"

    led.duty_cycle = 63000
    mouse.move(x=x, y=y)
    print(f"Mouse did {move_name} with coordinates ({x}, {y})")
    time.sleep(blink_interval)
    led.duty_cycle = 65000

    time.sleep(wait - blink_interval)

    state = (state + 1) % 4

print("Mouse mover stopped")