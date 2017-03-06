#!/usr/bin/env python

import unicornhat as unicorn
import time

import time
import sys
import os

from microdotphat import write_string, scroll, show


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

ipv4 = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
errorString = "ifup.."


#eyes
unicorn.set_pixel(1,2,255,0,0)
unicorn.set_pixel(1,3,255,0,0)
unicorn.set_pixel(2,2,255,0,0)
unicorn.set_pixel(2,3,255,0,0)
unicorn.set_pixel(5,2,255,0,0)
unicorn.set_pixel(5,3,255,0,0)
unicorn.set_pixel(6,2,255,0,0)
unicorn.set_pixel(6,3,255,0,0)

#eyebrow
unicorn.set_pixel(1,0,255,0,0)
unicorn.set_pixel(2,0,255,0,0)
unicorn.set_pixel(5,0,255,0,0)
unicorn.set_pixel(6,0,255,0,0)
unicorn.set_pixel(0,1,255,0,0)
unicorn.set_pixel(7,1,255,0,0)


unicorn.show()

#time.sleep(10)
 

#draw mouth
text = ipv4+ "   "

write_string(text, offset_x=0)

while True:
    scroll()
    show()
    time.sleep(0.08)


