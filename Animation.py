# This code was a modification of Sparkfun - update-a-graph-in-real-time.
# Modifications here allow a TMP36 Tempreture sensor inputs to be animated
# The TMP36 sensors are multiplexed using a 8 analog multiplexer {Custard Pi 3}
# via SPI. The Custard Pi 3 is based on MCP3208 which is a 8 channel 12-bit convertor
# A to D converter. See spec for more details.
# You need the file AI_sense.py in the same folder as this file.

#import sys
import RPi.GPIO as GPIO
import array as arr
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import AI_sense

# Set plot area for multiple plots
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

# Plot values
xs = []
ys0,ys1,ys2,ys3,ys4,ys5,ys6,ys7 = [],[],[],[],[],[],[],[]

# An array of floats starting value 0
AI = arr.array('f',[0,0,0,0,0,0,0,0])
x = 0
# Initialize communication with sensor e.g.TMP36
AI_sense.init() # Init file to import data TMP36

# Set axis ranges
ax1.set_ylim(-40,125)
ax1.set_xlim(0, 250)

# Set labels for plots
plt.title('Temperature v Time')
plt.ylabel('Temperature (deg C)')
plt.xlabel('Time')

#add grid
plt.grid(True)

# This function is called periodically from FuncAnimation
def animate(i):
#
# Read all 8 AI channels and save
    for x in range(8): 
        AI[x] = AI_sense.Read_One_AI(x)    # Pass our temp here
        AI[x] = round(AI[x])
#
# Test print - comment out if not required.
    if x == 7: 
        print (" AI ch0"," AI ch1", " AI ch2", " AI ch3", " AI ch4", " AI ch5", " AI ch6", " AI ch7", " degC") #print to screen
        print (" ", AI[0]," ", AI[1]," ", AI[2]," ", AI[3]," ", AI[4]," ", AI[5]," ", AI[6]," ", AI[7]) 

 #   print('Enables', En0, En1, En2)
# Save the value to plot - Time is i    
    xs.append(i)
    ys0.append(AI[0])
    ys1.append(AI[1])
    ys2.append(AI[2])
    ys3.append(AI[3])
    ys4.append(AI[4])
    ys5.append(AI[5])
    ys6.append(AI[6])
    ys7.append(AI[7])
    
# set color and line width for each input    
    ax1.plot(xs, ys0, color = "black", linewidth=0.5)
    ax1.plot(xs, ys1, color = "brown", linewidth=0.5)
    ax1.plot(xs, ys2, color = "red", linewidth=0.5)
    ax1.plot(xs, ys3, color = "orange", linewidth=0.5)
    ax1.plot(xs, ys4, color = "yellow", linewidth=0.5)
    ax1.plot(xs, ys5, color = "green", linewidth=0.5)


# This calls the animate above.
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
GPIO.cleanup()
