class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        count = Counter(nums)
        left = 0
        right = len(nums) -1
        lpos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                lpos = mid
                right = mid - 1
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        rpos = -1
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                rpos = mid
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return [lpos, rpos]
    