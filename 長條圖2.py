import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,4))
plt.title('Scores distribution of UNIX programming ')
x = np.arange(11)

plt.bar(x-0.2,[2,13,11,9,10,2,2,1,0,0,0],0.4,label='math')
plt.bar(x+0.2,[3, 9, 5, 8, 5, 1, 8, 7, 7, 2, 9],0.4,label='eng')
plt.legend()
plt.xticks(x,['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99','100'])
plt.show()