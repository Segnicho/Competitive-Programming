class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        tot = 0
        for num in nums:
            tot ^= num
            
        for num in nums:
            if num ^ tot == 0:
                return num