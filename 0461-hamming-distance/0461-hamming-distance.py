class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        count = 0
        
        while num >= 1:
            if num & 1:
                count += 1
            num >>= 1
            
        return count