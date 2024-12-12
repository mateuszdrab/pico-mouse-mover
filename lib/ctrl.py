# Read
from cptoml import fetch

# Write
from cptoml import put
from storage import remount

# Microcontroller
import microcontroller


# Toggle mouse mover
def toggle_mouse_mover(reset=True):
    mouse_moving = fetch("MOVE_MOVING")
    put("MOVE_MOVING", int(not mouse_moving))
    if reset:
        microcontroller.reset()

# from ctrl import toggle_mouse_mover; toggle_mouse_mover(reset=True)

# Enter safe mode
def safe_mode():
    microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
    microcontroller.reset()

# from ctrl import safe_mode; safe_mode()

# Auto toggle mouse mover
def auto_toggle_mouse_mover(enabled=True, reset=True):
    put("TOGGLE_ON_RESET", int(enabled))
    if reset:
        microcontroller.reset()

# from ctrl import auto_toggle_mouse_mover; auto_toggle_mouse_mover(enabled=True, reset=True)

# Function to allow customization of the MOVE_INTERVAL variable
def set_move_interval(interval=250, reset=True):
    put("MOVE_INTERVAL", interval)
    if reset:
        microcontroller.reset()

# from ctrl import set_move_interval; set_move_interval(interval=250, reset=True):

# Function to allow customization of the MOVE_STEP variable

def set_move_step(step=2, reset=True):
    put("MOVE_STEP", step)
    if reset:
        microcontroller.reset() 

# from ctrl import set_move_step; set_move_step(step=2, reset=True)