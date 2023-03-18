x = input().split()

for i in range(len(x)):
    x[i] = int(x[i])

'''if x[0] <= x[1] and x[0] <= x[2]:
    print(x[0])
elif x[1] <= x[0] and x[1] <= x[2]:
    print(x[1])
else:
    print(x[2])'''

'''x.sort()
print(x[0])'''

print(min(x))