import unicornhat as unicorn
import time

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)


#left eye
#unicorn.set_pixel(3,0,255,0,0)
#unicorn.set_pixel(4,0,255,0,0)


unicorn.set_pixel(2,1,255,0,0)
unicorn.set_pixel(5,1,255,0,0)

unicorn.set_pixel(1,2,255,0,0)
unicorn.set_pixel(6,2,255,0,0)

unicorn.set_pixel(0,3,255,0,0)
unicorn.set_pixel(7,3,255,0,0)


unicorn.show()

time.sleep(5)

