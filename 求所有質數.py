x = int(input())
list1 = []

for i in range(1,x+1):
    if (x % i) == 0:
        list1.append(i)
        
print(list1)