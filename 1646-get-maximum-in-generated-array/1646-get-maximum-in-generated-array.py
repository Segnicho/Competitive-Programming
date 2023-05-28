class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <2:
            return n
        res = [0, 1]
        for i in range(2,n+1):
            if not i%2:
                res.append(res[i//2])
            else:
                res.append(res[i//2]+ res[(i//2)+1])
        return max(res)
