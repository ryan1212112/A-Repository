def fac(n):
    if n >= 2:
        return fac(n-1)*n
    else:
        return 1

print(fac(int(input())))