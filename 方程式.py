import matplotlib.pyplot as plt
import numpy as np

x = np.arange(36,38)
y1 = -2*x+67
y2 = (62 - 3*x)/9
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()



'''
list1 = []
list2 = []



for i in range(-10000,10001):
    list1.append(i)
    list2.append(-i**2)
    
plt.plot(list1,list2)
plt.show()
'''