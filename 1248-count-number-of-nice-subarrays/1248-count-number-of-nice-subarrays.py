class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i] =0
            else:nums[i] = 1
        dikt = {0:1}
        res = 0
        prefSum =0
        for num in nums:
            prefSum += num
            res+=dikt.get(prefSum-k,0)
            if prefSum not in dikt:
                dikt[prefSum] = 1
            else:
                dikt[prefSum] += 1
        return res
       