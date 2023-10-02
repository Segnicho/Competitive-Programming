class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append(i*2 +1)
        
        avg = sum(arr)/n
        ops = 0
        
        for num in arr:
            ops += abs(num-avg)
        
        return int(ops/2)