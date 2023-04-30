matrix= [] 
n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input().split())))
sink = []
source = []
for row in range(n):
    cnt = 0
    for col in range(n):
        if matrix[row][col] != 0:
            cnt += 1
            break
    if cnt == 0:
        sink.append(row + 1)
        source.append(col + 1)
sink.sort()
source.sort()
print(len(source), *source)
print(len(sink), *sink)
