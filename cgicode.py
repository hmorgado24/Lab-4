#!/usr/bin/python37all
import cgi
import json

import cgitb
cgitb.enable()

data = cgi.FieldStorage()
LED = data.getvalue('LED')
s1 = data.getvalue('slider1')

L1 = 0
L2 = 0
L3 = 0

if (LED == '1'):
  L1 = s1
if (LED == '2'):
  L2 = s1
if (LED == '3'):
  L3 = s1

stats = {"LED1":L1, "LED2":L2, "LED3":L3}

with open('cgicode.txt', 'w') as f:  
  json.dump(stats, f)

print('Content-type: text/html\n\n')
print('<html>')
print('<meta http-equiv="refresh" content="30">')
print('<form action="/cgi-bin/cgicode.py" method="POST">')
print('<body>') 
print('<input type="radio" name="LED" value="1"> LED 1 <br>')
print('<input type="radio" name="LED" value="2"> LED 2 <br>')
print('<input type="radio" name="LED" value="3"> LED 3 <br>')
print('<input type="submit" value="Submit"> <br>')

print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED Brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</body>')
print('</html>')