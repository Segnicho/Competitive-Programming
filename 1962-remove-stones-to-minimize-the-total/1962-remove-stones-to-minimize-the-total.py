class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # change it to max heap
        for i, num in enumerate(piles):
            piles[i] = -num
            
        heapify(piles)
        for _ in range(k):
            val = -heappop(piles)
            val = ceil(val/2)
            heappush(piles, -val)
        
        return -sum(piles)