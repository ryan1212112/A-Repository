def fun(n):
    if n >= 2:
        return fun(n-1) + fun(n-2)
    else:
        return 1


print(fun(int(input())))