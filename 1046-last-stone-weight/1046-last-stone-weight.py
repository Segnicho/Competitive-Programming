class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            num1 = -heapq.heappop(heap)
            num2 = -heapq.heappop(heap)
            if num1 != num2:
                heapq.heappush(heap, num2- num1)
            
        return 0 if not heap else -heap[0]