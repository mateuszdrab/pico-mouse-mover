import time
import usb_hid
from adafruit_hid.mouse import Mouse
import os

mouse = Mouse(usb_hid.devices)

wait = os.getenv("MOVE_INTERVAL") / 1000
move_distance = os.getenv("MOVE_STEP")
mouse_moving = os.getenv("MOVE_MOVING")
state = 0

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

    mouse.move(x=x, y=y)
    print(f"Mouse did {move_name} with coordinates ({x}, {y})")
    time.sleep(wait)

    state = (state + 1) % 4

print("Mouse mover stopped")