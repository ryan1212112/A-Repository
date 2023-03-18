

x = int(input())
list1 = []


for i in range(1,x//2 + 1):
    list1.append([x - i,i])

list2 = list1.copy()

for z in range(len(list2)):
    y = 0
    for i in range(2,list2[z][y]):
        if list2[z][y] % i == 0:
            list1.remove(list2[z])
            break
    else:
        y = y + 1
        for i in range(2,list2[z][y]):
            if list2[z][y] % i == 0:
                list1.remove(list2[z])
                break
              
print(list1)