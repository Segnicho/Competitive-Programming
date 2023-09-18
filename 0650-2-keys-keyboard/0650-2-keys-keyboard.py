class Solution:
    def minSteps(self, n: int) -> int:
        
        def recur(num):
            for i in range(2, int(sqrt(num))+1):
                if num%i == 0:
                    return int(recur(num/i)) + i 
            return int(num)
        if n == 1:
            return 0
        return recur(n)
        
