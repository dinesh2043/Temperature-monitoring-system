import serial
import time

import plotly
import numpy as np 
import plotly.plotly as py  
import plotly.tools as tls   
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='dinsap', api_key='kxuvbdflrh')

ser = serial.Serial(
    port='/dev/ttyUSB1',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
#line = []
temp_str = ""

while True:
    for c in ser.read():
        if c == ' ':
	   #line = line
	   temp_str = temp_str
	#to cast str to float use float(temp_str)
        elif c == '\n':
            print("Temperature: ",float(temp_str))
	    print("Time: ",time.strftime("%H:%M:%S"))
	    temp_str = ""
            #line = []
            #break
	else:
	    #line.append(c)
	    temp_str+=str(c)



ser.close()
