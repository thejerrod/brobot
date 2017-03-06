#!/usr/bin/env python

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.3)

x = 1
while True:

#left eye
 unicorn.set_pixel(0,0,255,0,0)
 unicorn.set_pixel(0,3,255,0,0)

 unicorn.set_pixel(1,1,255,0,0)
 unicorn.set_pixel(1,2,255,0,0)

 unicorn.set_pixel(2,1,255,0,0)
 unicorn.set_pixel(2,2,255,0,0)

#right eye
 unicorn.set_pixel(5,1,255,0,0)
 unicorn.set_pixel(5,2,255,0,0)

 unicorn.set_pixel(6,1,255,0,0)
 unicorn.set_pixel(6,2,255,0,0)

 unicorn.set_pixel(7,0,255,0,0)
 unicorn.set_pixel(7,3,255,0,0)

 unicorn.show()
 time.sleep(5)

x += 1
