# Simple Pi Pico USB Mouse Mover

Simple mouse mover which can be controlled from the REPL shell.

Each time the board is reset, the state of enablement of the mover will toggle.

I'm using it with the RP2040 USB-A development module from [AliExpress](https://www.aliexpress.com/item/1005006710298380.html) and I'm quite happy with the results so far

<img src="https://ae-pic-a1.aliexpress-media.com/kf/Sa8cd157ec37d47799a839609d0594e0af.jpg_960x960q75.jpg_.avif" alt="RP2040 USB-A development module" width="200"/>

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

To disable auto toggling of the mouse mover on reset, you can run the below:

```python
from ctrl import auto_toggle_mouse_mover
auto_toggle_mouse_mover(False)
```

Set MOVE_INTERVAL and MOVE_STEP with the below code
Set reset=False to not reset the board after setting the values so you can set both at once

```python
from ctrl import set_move_interval, set_move_step
set_move_interval(250) # 0.25 second in milliseconds
set_move_step(2) # 2 pixels at a time
```
