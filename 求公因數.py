x = [int(input()),int(input())]

list1 = [[],[]]

for z in range(2):
    for i in range(1,x[z]+1):
        if (x[z] % i) == 0:
            list1[z].append(i)
            

list2 = []

for i in range(len(list1[0])):
    if list1[0][i] in list1[1]:
        list2.append(list1[0][i])

print(list2[-1])