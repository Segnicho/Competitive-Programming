def helper():
    n = int(input())
    count = 0
    for i in range(n):
        r = (input().split())
        for j in range(i):
            if r[j] =="1":
                count+=1
    return count
print(helper())
