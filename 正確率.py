import numpy as np
temp = 0

for i in range(100):
    事實 = np.random.randint(0,2,60)
    預測 = np.random.rand(60)
    
    預測01 = 預測 < 0.7
    
    結果 = 預測01 == 事實
    temp += 結果.sum() / 60

print(temp/100)