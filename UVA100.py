x = int(input())
y = int(input())

def cl (i):
    k = 1
    while not i == 1:
        if not i % 2 == 0:
            i = 3*i + 1
        else:
            i = i/2
        k += 1
    return(k)

if x > y:
    x,y = y,x

j = 0
     
for i in range(x,y+1):
    a = cl(i)
    if a > j:
        j = a

print(j)