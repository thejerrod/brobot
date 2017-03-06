import requests
import time
import sys
from microdotphat import write_string, scroll, show


#pull 24hr avg btc rice from btc charts api
r = requests.get('http://api.bitcoincharts.com/v1/weighted_prices.json')
data = r.json()
averageBTC = data['USD']['24h']

#print('BTC USD 24hr:'), averageBTC
print("""Scrolling BTC counter

Press Ctrl+C to exit.
""".format(name=sys.argv[0]))

text = averageBTC + "   "

write_string(text, offset_x=0)

while True:
    scroll()
    show()
    time.sleep(0.08)

