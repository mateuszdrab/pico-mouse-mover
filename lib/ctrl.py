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

# from ctrl import toggle_mouse_mover; toggle_mouse_mover()

# Enter safe mode
def safe_mode():
    microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
    microcontroller.reset()

# from ctrl import safe_mode; safe_mode()