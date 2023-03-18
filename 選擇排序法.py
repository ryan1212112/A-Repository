list_var = [12, 28, 5, 33]

n = len(list_var)

print(n)

for i in range(n-1):
    minInder = i
    for j in range(i+1,n):
        if list_var[j] < list_var[minInder]:
                minInder = j
        list_var[minInder],list_var[i] = list_var[i],list_var[minInder]

print(list_var)