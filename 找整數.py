x = int(input())

list1 = []

for i in range(2,x + 1):
    list1.append(i)


list2 = list1.copy()

for i in range(2,x+1):
    for y in range(x-1):
            if not list1[y] == i and list1[y] % i == 0:
                if list1[y] in list2:
                    list2.remove(list1[y])

print(list2)