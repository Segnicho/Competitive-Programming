n = int(input())
for _ in range(n):
    arrlen = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    for i in range(arrlen-1):
        diff = abs(arr[i+1]) - abs(arr[i])
        if diff > 1:
            print("NO")
            break
    else:
        print("YES")
