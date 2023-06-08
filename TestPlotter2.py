import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#  plotting area
x1 =  0    #start
x2 = 150    #end
y1 = 0
y2 = 110
plt.axis([x1,x2,y1,y2])

plt.axis('on')
plt.grid(True)

#Axis
plt.xlabel('X Lable')
plt.ylabel('Y Lable')
# The Title
plt.title('Title Sample')

#Tick Marks
dx = 1  #spacing
dy = 1

#for x in np.arange(x1,x2,dx):     #x locations
 #   for y in np.arange(y1,y2,dy): #y locations
  #      plt.scatter(x,y,s=1,color = 'blue') #plot grey grid points

#On screen
plt.show()

