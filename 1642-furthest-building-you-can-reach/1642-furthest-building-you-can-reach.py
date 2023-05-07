class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        n = len(heights)
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff <= 0:
                continue
            ladders -= 1
            diff > 0 and heappush(heap, diff)
            if ladders < 0:
                bricks -= heappop(heap)
            if bricks < 0:
                return i - 1
        return len(heights) - 1