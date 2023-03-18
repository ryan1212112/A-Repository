x = int(input())

while True:
    print(x % 10)
    x = x // 10
    if not x > 0:
        break