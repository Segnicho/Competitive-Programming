class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        m = n = len(matrix) 
        heap = []
        for j in range(m):
            heap.append([matrix[0][j], 0, j])
        for _ in range( k):
            num, r, col = heappop(heap)
            if r+1 < n:
                heappush(heap, [matrix[r+1][col], r+1, col])
        return num