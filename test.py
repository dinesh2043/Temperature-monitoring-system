import plotly 
import certifi
import urllib3

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
plotly.tools.set_credentials_file(username='dinsap', api_key='0l2j9xmxa3')

import numpy as np 
import plotly.plotly as py  
import plotly.tools as tls   
import plotly.graph_objs as go

import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
#line = []
temp_str = ""

#set stream_ids
f = []
f.append('ovm08xi3v8')

tls.set_credentials_file(stream_ids=f)

stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list 
stream_id = stream_ids[0]
# Make instance of stream id object 
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)

# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Time series')

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()


# (*) Import module keep track and format current time
import datetime 
import time   

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5) 

while True:

	for c in ser.read():
		if c == ' ':
		   #line = line
		   temp_str = temp_str
		#to cast str to float use float(temp_str)
		elif c == '\n':
		    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		    y = temp_str
		    print("Temperature: "+ temp_str)
		    print("Time: ",time.strftime("%H:%M:%S"))
		    temp_str = ""
		    # Send data to your plot
	    	    s.write(dict(x=x, y=y))  
	    
	    	    #     Write numbers to stream to append current data on plot,
	    	    #     write lists to overwrite existing data on plot
		    
	    	    time.sleep(2)  # plot a point every second    
		    #line = []
		    #break
		else:
		    #line.append(c)
		    temp_str+=str(c)
 
# Close the stream when done plotting
s.close() 

# Embed never-ending time series streaming plot
tls.embed('streaming-demos','12')

ser.close()


