class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        def bt(n, val):
            if n == 0:
                return 1
            if n == 1:
                return 9
            
            return val*bt(n-1, val-1)
        
        res = 0
        for i in range(n+1):
            res += bt(i, 9)
        return res