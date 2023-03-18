a,b = int(input()),int(input()) 

a,b = max(a,b),min(a,b)

while a > 0 and b > 0:
    a = a % b
    if a > 0:    
        b = b % a

print(max(a,b))
