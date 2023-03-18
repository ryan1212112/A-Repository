import matplotlib.pyplot as plt
import numpy as np

list1 = [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
list1= np.array(list1)

x = list1[:,0]
y = list1[:,1]

plt.plot(x,y,'ro')
plt.show()