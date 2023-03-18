'''
x = input()

xlist = list(x)
x1 = 0

for i in range(len(xlist)):
    x1 = x1 + int(xlist[i]) ** len(xlist)


if x1 == int(x):
    print('是')
else:
    print('不是')
'''

x = int(input())
xc = x
xlist = []

while x > 0:
    xlist.append(x % 10)
    x = x // 10
    
i = 0

while i < len(xlist):
    x = x + xlist[i] ** len(xlist)
    i = i + 1

if xc == x:
    print('T')
else:
    print('F')
