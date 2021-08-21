import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01) #x从0到派(3.1415926)*2
y=np.tan(x)
y=1/y
plt.plot(x,y)
plt.show()