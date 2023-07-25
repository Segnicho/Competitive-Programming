tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    l, r = 0, 0
    curr = arr[0]
    while r < n:
        if arr[l] * arr[r] > 0:
            curr = max(curr, arr[r])
            r += 1
        else:
            ans +=  curr
            l  = r
            curr = arr[l]
    ans += curr
    print(ans)
