from numpy import random
import time

random.seed(int(time.time()))

答案 = random.randint(10000)

while True:
    x = int(input('輸入要猜的數:'))
    if x == 答案:
        print('答對了😉')
        break
    elif x > 答案:
        print('太大了')
    else:
        print('太小了')