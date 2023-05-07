class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for ls in matrix:
            for num in ls:
                heappush(nums, num)
        for _ in range(1, k):
            heappop(nums)
        return nums[0]