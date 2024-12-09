import random
import storage
import supervisor
import os

storage.remount("/", readonly=False)
print("Storage remounted read-write, USB storage will be read-only")

storage.disable_usb_drive()
print("USB drive disabled as not in safe mode")

if os.getenv("TOGGLE_ON_RESET"):
    from ctrl import toggle_mouse_mover
    toggle_mouse_mover(False)
    print("Mouse mover toggled")