class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in set(nums):
            return [-1, -1]
        count = Counter(nums)
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        return [left, left + count[nums[left]] - 1]