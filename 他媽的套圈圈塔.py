def hanoi(n,start,mid,end):
    if n == 1:
        print("Move disk",n,"from source",start,"to destination",end)
        return None
    #n-1->mid
    hanoi(n-1,start,end,mid)
    #n
    print("Move disk",n,"from source",start,"to destination",end)
    #n-1
    hanoi(n-1,mid,start,end)