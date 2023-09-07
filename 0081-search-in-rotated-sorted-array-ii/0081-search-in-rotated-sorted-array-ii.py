class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in set(nums)
        arr = nums[:]
        nums = []
        st = set()
        for num in arr:
            if num not in st:
                st.add(num)
                nums.append(num)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                 return True
            elif nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False