#!/usr/bin/python37all
import cgi
import json
import RPi.GPIO as GPIO

import cgitb
cgitb.enable()

ledpin1 = 13
ledpin2 = 19
ledpin3 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin1, GPIO.OUT)
GPIO.setup(ledpin2, GPIO.OUT)
GPIO.setup(ledpin3, GPIO.OUT)

data = cgi.FieldStorage()
L1 = data.getvalue('LED')
s1 = data.getvalue('slider1')
data = {"LED":L1, "slider1":s1}

with open('cgicode.txt', 'w') as f:  
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<meta http-equiv="refresh" content="30">')
print('<body>') 
print('<LED = " + data.getvalue("LED")><br>')
print('<form action="/Lab-4/cgicode.py" method="POST">')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED Brightness">')
print('</form>')
print(‘Brightness = %s' % s1)


print('</body>')
print('</html>')