class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = len(nums)-1
        l = 0
        cnt = 0
        while l < r:
            sm = nums[l] + nums[r]
            if sm < k:
                l+=1
            elif sm > k:
                r-=1
            else:
                cnt+=1
                l+=1
                r-=1
        return cnt
