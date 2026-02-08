
import numpy as np

#Library to plot
import matplotlib.pyplot as plt

#create list starting from 0 to 2pi with 100 points in between
x = np.linspace(0,2*np.pi,100)
print(x)

#Create array of sin values of x
y = np.sin(x)
print(y)

#Plot the x and y values on graph and then display
plt.plot(x,y)
plt.show()