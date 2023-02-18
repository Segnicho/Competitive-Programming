def helper():
    leng1, leng2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res = []
    j = 0
    
    for num in arr2:
        while j < leng1 and arr1[j] < num:
            j += 1
        res.append(j) 
    print(*res)
 
helper()
