#!/usr/bin/python37all
import cgi
import json

import cgitb
cgitb.enable()

data = cgi.FieldStorage()

L1 = data.getvalue('LED')
s1 = data.getvalue('slider1')
stats = {'LED':L1, 'slider1':s1}

with open('jsonstor.txt', 'w') as f:  
  json.dump(stats, f)

print('Content-type: text/html\n\n')
print('<html>')
print('<meta http-equiv="refresh" content="30">')
print('<form action="/cgi-bin/cgicode.py" method="POST">')
print('<input type="radio" name="LED" value="1"> LED 1 <br>')
print('<input type="radio" name="LED" value="2"> LED 2 <br>')
print('<input type="radio" name="LED" value="3"> LED 3 <br>')

print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED Brightness">')
print('</form>')
print('</html>')