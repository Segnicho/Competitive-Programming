class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right  = len(nums) - 1
        # return 2
        nums.append(float("-inf"))
        while left <= right:
            mid = (left + right)//2
            print(mid)
            if nums[mid] > nums[mid-1]:
                left = mid + 1
            elif nums[mid-1] > nums[mid]:
                right = mid - 1
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
        return right