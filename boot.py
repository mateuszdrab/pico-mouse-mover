import random
import storage
import supervisor

storage.remount("/", readonly=False)
print("Storage remounted read-write, USB storage will be read-only")

if supervisor.runtime.safe_mode_reason == supervisor.SafeModeReason.NONE:
    storage.disable_usb_drive()
    print("USB drive disabled as not in safe mode")


from ctrl import toggle_mouse_mover
toggle_mouse_mover(False)