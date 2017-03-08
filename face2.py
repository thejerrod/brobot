#!/usr/bin/env python

#this is the main brobot face script
#it displays a default face (face 0) until some action occurs
#actions could be push notifications (twitter, irc, btc threshold, boot process, ec)
#trying to keep cpu in mind here because the pi zero is only single core 1ghz. 
#animation refreshes need to be scaled back, and "eyes" are only drawn once unless animated.

import math
import unicornhat as unicorn
import time
import sys
import os
import requests


from microdotphat import clear, write_string, scroll, show, set_brightness, WIDTH, HEIGHT

face = 0
#text = "Brobot v1.0 "

btc = 1
twitter = "none"
ipFace = 0
boot=0
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)


def set_face( face_status ):
	if ( face_status == 0 ):
		speed = 5
		string = 0
		shown = True
		strings = ["Brobot", "#Bro", "+plus+", "#Bot"]

		#boot eyes
		unicorn.set_pixel(1,2,255,0,0)
		unicorn.set_pixel(1,3,255,0,0)

		unicorn.set_pixel(2,2,255,0,0)
		unicorn.set_pixel(2,3,255,0,0)

		unicorn.set_pixel(5,2,255,0,0)
		unicorn.set_pixel(5,3,255,0,0)

		unicorn.set_pixel(6,2,255,0,0)
		unicorn.set_pixel(6,3,255,0,0)
		unicorn.show()

		#boot mouth (brobot fading text)
		show()

		# Start time. Phase offset by math.pi/2
		start = time.time()
		while True:
		    # Fade the brightness in/out using a sine wave
		    b = (math.sin((time.time() - start) * speed) + 1) / 2
		    set_brightness(b)
	
		    # At minimum brightness, swap out the string for the next one
		    if b < 0.002 and shown:
		        clear()
		        write_string(strings[string], kerning=False)

		        string += 1
		        string %= len(strings)
	
		        show()
		        shown = False

		    # At maximum brightness, confirm the string has been shown
		    if b > 0.998:
		        shown = True

		    # Sleep a bit to save resources, this wont affect the fading speed
		    time.sleep(0.01)	

	elif ( face_status == 1 ):
		#ipface eyes
		unicorn.set_pixel(1,2,255,0,0)
		unicorn.set_pixel(1,3,255,0,0)
		unicorn.set_pixel(2,2,255,0,0)
		unicorn.set_pixel(2,3,255,0,0)
		unicorn.set_pixel(5,2,255,0,0)
		unicorn.set_pixel(5,3,255,0,0)
		unicorn.set_pixel(6,2,255,0,0)
		unicorn.set_pixel(6,3,255,0,0)

		#ipface eyebrows
		unicorn.set_pixel(1,0,255,0,0)
		unicorn.set_pixel(2,0,255,0,0)
		unicorn.set_pixel(5,0,255,0,0)
		unicorn.set_pixel(6,0,255,0,0)
		unicorn.set_pixel(0,1,255,0,0)
		unicorn.set_pixel(7,1,255,0,0)
 		#draw eyes (square beady)
		unicorn.show()
		#draw mouth (scrolling text)
		ipv4 = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
		text = ipv4+ "   "
		write_string(text, offset_x=0)

		while True:
		    scroll()
		    show()
		    time.sleep(0.08)

	elif ( face_status == 2 ):
		#btc eyes
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
		#draw eyes
		unicorn.show()

		#btc mouth
		r = requests.get('http://api.bitcoincharts.com/v1/weighted_prices.json')
		data = r.json()		
		averageBTC = data['USD']['24h']
		text = averageBTC + "   "
		write_string(text, offset_x=0)

		while True:
		    scroll()
		    show()
		    time.sleep(0.08)		

while True:
	if (boot == 1):
		face = 0
        elif (ipFace == 1):
                face = 1
        elif (btc == 1 ):
                face = 2
 
        # Face variable set, send to function for processing
        set_face( face )






