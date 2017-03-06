#!/usr/bin/env python

import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)


#eyes
unicorn.set_pixel(1,2,255,0,0)
unicorn.set_pixel(1,3,255,0,0)

unicorn.set_pixel(2,2,255,0,0)
unicorn.set_pixel(2,3,255,0,0)

unicorn.set_pixel(5,2,255,0,0)
unicorn.set_pixel(5,3,255,0,0)

unicorn.set_pixel(6,2,255,0,0)
unicorn.set_pixel(6,3,255,0,0)

#brow
#unicorn.set_pixel(0,0,255,0,0)
#unicorn.set_pixel(0,1,255,0,0)
#unicorn.set_pixel(3,1,255,0,0)
#unicorn.set_pixel(4,1,255,0,0)


#unicorn.set_pixel(1,0,255,0,0)
#unicorn.set_pixel(2,0,255,0,0)
#unicorn.set_pixel(5,0,255,0,0)
#unicorn.set_pixel(6,0,255,0,0)

#unicorn.set_pixel(0,1,255,0,0)

#unicorn.set_pixel(7,1,255,0,0)




unicorn.show()

time.sleep(10)

