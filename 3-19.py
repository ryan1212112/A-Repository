
x = [['WU Dajing', 'HWANG Daeheon', 'LIM Hyo Jun', 'Samuel GIRARD'], 
 ['6.63', '6.74', '6.73', '6.92'], ['8.52', '8.57', '8.63', '8.61'], 
 ['8.04', '8.07', '8.16', '8.11'], ['8.09', '8.07', '8.01', '8.06'], 
 ['8.30', '8.40', '8.38', '8.28']]

y = []

#將選手全部成績相加並存入list
for i in [0,3,1,2]:
    y.append(float(x[1][i]) + float(x[2][i]) + float(x[3][i]) + float(x[4][i]))
    
print(y)

y.sort()
print(y)