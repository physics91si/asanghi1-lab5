#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,np.pi,0.01)
y=np.sin(x)
plt.plot(x,y)
plt.show()
# TODO fill in this function
def integrate(y, dx):
    return sum(dx * y)
print(integrate(y,0.01))

cosY=np.cos(x)

print("cos() integrated 0 to pi; dx=0.01")
print(integrate(cosY,0.01))

import scipy.integrate as inte

f= lambda t: np.sin(t)
print(inte.quad(f,0,np.pi))
f2= lambda n: np.cos(n)
print(inte.quad(f2,0,np.pi))


# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y
