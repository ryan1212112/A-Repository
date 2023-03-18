import matplotlib.pyplot as plt
from numpy import arange as npar

F = open("D:\下載\新增 文字文件.txt")
txt = F.readlines()
count1 = [0 for i in range(11)]
count2 = [0 for i in range(11)]
SR = [i for i in range(9,100,10)]
SR.append(100)

for i in range(1,len(txt)):
    txt[i] = txt[i].split()
    for y in range(len(SR)):
        if int(txt[i][1]) <= int(SR[y]):
            if y > 0:
                if int(txt[i][1]) > int(SR[y-1]):
                    count1[y] += 1
            else:
                count1[y] += 1
        if int(txt[i][2]) <= int(SR[y]):
            if y > 0:
                if int(txt[i][2]) > int(SR[y-1]):
                    count2[y] += 1
            else:
                count2[y] += 1

plt.figure(figsize=(8,4))
plt.title('Scores distribution')
x = npar(11)

plt.bar(x-0.2,count1,0.4,label='Math')
plt.bar(x+0.2,count2,0.4,label='Science')
plt.legend()
plt.xticks(x,['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99','100'])
plt.show()

'''
老師的作法
import matplotlib.pyplot as plt
import numpy as np

f = open('scores.txt', 'r')
text = f.read()
lines = text.split('\n')[:-1]
f.close()

mat_count = [0 for i in range(11)]
sci_count = [0 for i in range(11)]

first_line = lines[0].split('\t')
for line in lines[1:]:
    stu, mat, sci = line.split('\t')
    mat_count[int(mat)//10] += 1
    sci_count[int(sci)//10] += 1

xbar = ['{0}-{1}'.format(i, i+9) for i in range(0, 100, 10)]
xbar.append('100')
#plt.bar(xbar, mat_count, label=first_line[1])
#plt.bar(xbar, sci_count, label=first_line[2])
xaxis = np.arange(11)
plt.xticks(xaxis, xbar)
plt.bar(xaxis -  0.2, mat_count, 0.4, label=first_line[1])
plt.bar(xaxis +  0.2, sci_count, 0.4, label=first_line[2])
plt.legend()
plt.title('Midterm score distribution of Class 304')
plt.show() 
'''
