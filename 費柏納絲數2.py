x = int(input())
list1 = []

for i in range(x):
    if i >= 2:
        list1.append(list1[i-1] + list1[i-2])
    else:
        list1.append(1)
        
print(list1)