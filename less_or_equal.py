n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0
res = 0
if k == 0:
    res = arr[0]-1
else:
    res = arr[k-1]
for num in arr:
    if num <= res:
        cnt  += 1
    else:
        break
if cnt  != k or res < 1 or res > 10**9:
    print("-1")
else:
     print(res)
