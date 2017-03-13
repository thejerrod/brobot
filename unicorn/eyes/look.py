#!/usr/bin/env python

# script to help brobot's eyes look around, with blinking action

import unicornhat as unicorn
import time
import random

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

count = 0
blink = 0
while count < 5:
        n = random.randrange(0,6)
	m = random.randrange(0,3)
        #set eyes
        print(count)
	unicorn.clear()
	unicorn.set_pixel(1,2,255,0,0)
	unicorn.set_pixel(1,3,255,0,0)
	unicorn.set_pixel(2,2,255,0,0)
	unicorn.set_pixel(2,3,255,0,0)

	unicorn.set_pixel(5,2,255,0,0)
	unicorn.set_pixel(5,3,255,0,0)
	unicorn.set_pixel(6,2,255,0,0)
	unicorn.set_pixel(6,3,255,0,0)

        if blink == 4:
	        print "blink blink"

                #eyes blink
                unicorn.set_pixel(1,2,0,0,0)
                unicorn.set_pixel(2,2,0,0,0)
                unicorn.set_pixel(5,2,0,0,0)
                unicorn.set_pixel(6,2,0,0,0)

                unicorn.show()
                time.sleep(.05)
                #eyes on for random value from above
                unicorn.set_pixel(1,2,255,0,0)
                unicorn.set_pixel(2,2,255,0,0)
                unicorn.set_pixel(5,2,255,0,0)
                unicorn.set_pixel(6,2,255,0,0)
                unicorn.show()
                time.sleep(m+1)

                #off again
                unicorn.set_pixel(1,2,0,0,0)
                unicorn.set_pixel(2,2,0,0,0)
                unicorn.set_pixel(5,2,0,0,0)
                unicorn.set_pixel(6,2,0,0,0)
                unicorn.show()
                time.sleep(.05)

                #back on
                unicorn.set_pixel(1,2,255,0,0)
                unicorn.set_pixel(2,2,255,0,0)
                unicorn.set_pixel(5,2,255,0,0)
                unicorn.set_pixel(6,2,255,0,0)
                unicorn.show()
                time.sleep(n)
#                blink= 0


	unicorn.show()
	time.sleep(1)
	count += 1
	blink += 1
        if count == 5:
                print "look left"
                #eyes left
		unicorn.clear()
		unicorn.set_pixel(0,2,255,0,0)
		unicorn.set_pixel(0,3,255,0,0)
		unicorn.set_pixel(1,2,255,0,0)
		unicorn.set_pixel(1,3,255,0,0)

		unicorn.set_pixel(4,2,255,0,0)
		unicorn.set_pixel(4,3,255,0,0)
		unicorn.set_pixel(5,2,255,0,0)
		unicorn.set_pixel(5,3,255,0,0)

                unicorn.show()
                time.sleep(n+1)
               
		#eyes center
		print "eyes center"
	        unicorn.clear()
	        unicorn.set_pixel(1,2,255,0,0)
	        unicorn.set_pixel(1,3,255,0,0)
	        unicorn.set_pixel(2,2,255,0,0)
	        unicorn.set_pixel(2,3,255,0,0)

	        unicorn.set_pixel(5,2,255,0,0)
	        unicorn.set_pixel(5,3,255,0,0)
	        unicorn.set_pixel(6,2,255,0,0)
	        unicorn.set_pixel(6,3,255,0,0)

                unicorn.show()
                time.sleep(n+2)
		if blink == 5:
	                print "blink blink"

	                #eyes blink
	                unicorn.set_pixel(1,2,0,0,0)	
	                unicorn.set_pixel(2,2,0,0,0)
	                unicorn.set_pixel(5,2,0,0,0)
	                unicorn.set_pixel(6,2,0,0,0)

	                unicorn.show()
	                time.sleep(.05)
	                #eyes on for random value from above
	                unicorn.set_pixel(1,2,255,0,0)
	                unicorn.set_pixel(2,2,255,0,0)
	                unicorn.set_pixel(5,2,255,0,0)
	                unicorn.set_pixel(6,2,255,0,0)	
	                unicorn.show()
	                time.sleep(m+1)

	                #off again
	                unicorn.set_pixel(1,2,0,0,0)
	                unicorn.set_pixel(2,2,0,0,0)
	                unicorn.set_pixel(5,2,0,0,0)
	                unicorn.set_pixel(6,2,0,0,0)
	                unicorn.show()
	                time.sleep(.05)

	                #back on
	                unicorn.set_pixel(1,2,255,0,0)
	                unicorn.set_pixel(2,2,255,0,0)
	                unicorn.set_pixel(5,2,255,0,0)
	                unicorn.set_pixel(6,2,255,0,0)
	                unicorn.show()
	                time.sleep(n)
	                blink= 0

                #eyes right
		print "eyes right"
		unicorn.clear()
		unicorn.set_pixel(2,2,255,0,0)
		unicorn.set_pixel(2,3,255,0,0)
		unicorn.set_pixel(3,2,255,0,0)
		unicorn.set_pixel(3,3,255,0,0)

		unicorn.set_pixel(6,2,255,0,0)
		unicorn.set_pixel(6,3,255,0,0)
		unicorn.set_pixel(7,2,255,0,0)
		unicorn.set_pixel(7,3,255,0,0)

                unicorn.show()
                time.sleep(n+1)

                count = 0













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




#unicorn.show()

#time.sleep(10)

