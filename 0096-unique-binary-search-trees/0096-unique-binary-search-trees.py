class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def findFact(num):
            if num <= 1:
                return 1
            return num*findFact(num-1)
        return findFact(2*n)//(findFact(n+1) * findFact(n))