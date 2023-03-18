y = int(input())

for i in range(y):
    x = int(input())
    if x % 4 == 0 and x % 100 or x % 100 == 0 and x % 400 == 0:
        print('閏年')
    else:
        print('平年')