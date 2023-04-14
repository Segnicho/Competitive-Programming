from collections import defaultdict

def helper():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        row = (input().split())
        for j in range(len(row)):
            if row[j] == "1":
                graph[i+1].append(j+1)
    for i in range(1,n +1):
        graph[i].sort()
        print(len(graph[i]), *graph[i])

helper()
