def getTotalX(a, b):
    # Write your code here
    
    firstans = []
    secondans = []
    i = a[len(a)-1]
    j = b[0]
    x = 0
    for x in range(i, j):
        for item in a:
            print(x, item)
            if x % item != 0:
                del(item)
        print(a)
    ans = set(firstans)  

    for x in b:
        for item in ans:
            if x % item == 0:
                secondans.append(item) 

    print(ans)
    print(secondans)
    print(set(secondans))
    return len(set(secondans))                

print(getTotalX([2, 6], [24, 36]))
# print(getTotalX([2, 4], [16, 32, 96]))