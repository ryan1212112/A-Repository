def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
           return False
    else:
        return True




x = int(input())
answer = []

for i in range(1,x//2 + 1):
    if isPrime(i) and isPrime(x-i):
        answer.append([i,x-i])

print(answer)