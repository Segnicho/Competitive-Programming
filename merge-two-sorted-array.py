def helper():
    leng1, leng2 = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    merged = []
    i = 0
    j = 0

    # while i < leng1  or j < leng2:
    #     if j == leng2 or i< leng1 and (arr1[i] < arr2[j]):
    #         merged.append(arr1[i])
    #         i += 1
    #     else:
    #         merged.append(arr2[j])
    #         j += 1

    arr1.append(float("inf"))
    arr2.append(float("inf"))

    while i<=leng1 and j<= leng2:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    merged.pop()
    print(*merged)
helper()
