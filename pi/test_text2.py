from OLED import OLED
from OLEDWindow import OLEDWindow
import time

# The OLED hardware driver
oled = OLED()

window_one = OLEDWindow(oled,0,0,256,64)

#for y in xrange(4):
#    mes = ""
#    for x in xrange(32):
#        mes = mes + chr(y*32+x) 
#    window_one.draw_text(0,y*8,mes,15)
    
#window_one.draw_big_text(0,0,"Big and dim!",2)
#
#window_one.draw_screen_buffer()
#
#window_one.draw_big_text(0,0,"Hello World  ",1)
#time.sleep(5)
#window_one.draw_screen_buffer()
counter = 0
while True:
    window_one.draw_text(0,0,str(counter),10)
    window_one.draw_screen_buffer()
    counter = counter + 1
    #time.sleep(.01)
