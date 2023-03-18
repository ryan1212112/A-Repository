from numpy import random

x = random.choice(10,4,False)
A = 0

while A < 4:
    y = input('輸入要猜的數:')
    
    A = 0 #位置正確
    B = 0 #存在
    
    for i in range(4):
        if int(y[i]) in x:
            if int(y[i]) == x[i]:
                A += 1
            else:
                B += 1
    print('A' + str(A) + 'B' + str(B))
    
print('正確')