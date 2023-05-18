class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                return True
            mp[num] = 1
        return False
            