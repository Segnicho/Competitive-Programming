class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        tot = 0
        for i in range(n):
            tot += (i*2 +1)
        
        avg = tot/n
        ops = 0
        
        for i in range(n):
            num = i*2 +1
            ops += abs(num-avg)
        
        return int(ops/2)