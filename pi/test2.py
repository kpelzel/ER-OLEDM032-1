from OLED import OLED
from OLEDWindow import OLEDWindow

# The OLED hardware driver
oled = OLED()

# Two windows on the screen. One is the entire screen. The
# other is a small square over to the right
window_one = OLEDWindow(oled,0,0,256,64)

for i in range(255):
    window_one.set_pixel(i,0,i)
window_one.draw_screen_buffer()