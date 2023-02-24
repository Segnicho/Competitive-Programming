class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        tot = 0
        res = 0
        for num in nums:
            tot+=num
            res += mp.get(tot - k, 0 )
            mp[tot] = 1 + mp.get(tot,0)
        return res

        
