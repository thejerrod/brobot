#!/usr/bin/env python

import time
import sys
import os

from microdotphat import write_string, scroll, show

ipv4 = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
errorString = "ifup.."

#what happens if theres no network
# if ipv4 = error
#   flash(errorString)

print("""Scrolling IP Address Test

Press Ctrl+C to exit.
""".format(name=sys.argv[0]))

text = ipv4+ "   "

write_string(text, offset_x=0)

while True:
    scroll()
    show()
    time.sleep(0.08)
