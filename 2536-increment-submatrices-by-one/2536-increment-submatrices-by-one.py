class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0 for _ in range(n+2)] for i in range(n+2)]
        queries.sort()
        for x1, y1, x2, y2 in queries:
            for i in range(x2-x1+1):
                arr[x1+1+i][y1+1] += 1
                arr[x1+1+i][y2+2] -= 1
        for row in arr:
            for i in range(1, len(row)):
                row[i]+=row[i-1]
        arr.pop()
        arr.pop(0)
        for rw in arr:
            rw.pop()    
            rw.pop(0)    
        return arr