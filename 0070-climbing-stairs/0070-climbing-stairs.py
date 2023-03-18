class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def recur(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return recur(n-1) + recur(n-2)
        return recur(n)
    