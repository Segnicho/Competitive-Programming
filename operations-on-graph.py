from collections import defaultdict
def helper():
    n = int(input())
    ops = int(input())
    graph = defaultdict(list)
    for i in range(ops):
        row = list(map(int, input().split()))
        if len(row) == 3:
            graph[row[1]].append(row[2])
            graph[row[2]].append(row[1])
        else:
            if graph[row[1]]:
                print(*graph[row[1]])
            else:
                print()
helper()
