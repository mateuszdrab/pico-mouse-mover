# Simple Pi Pico USB Mouse Mover

Simple mouse mover which can be controlled from the REPL shell.

Each time the board is reset, the state of enablement of the mover will toggle.

You can also change this manually in the REPL shell and the board will reboot:

```python
from ctrl import toggle_mouse_mover
toggle_mouse_mover()
```

By default, USB storage is not presented unless booting in safe mode which can be entered by typing the below:
  
```python
from ctrl import safe_mode
safe_mode()
```
