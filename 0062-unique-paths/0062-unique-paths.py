class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        def dp(i, j):
            if i == m-1 and n-1 == j:
                return 1
            if i > m-1 or j > n-1:
                return 0
            state = (i, j)
            if state not in memo:
                memo[state] = dp(i+ 1,  j) + dp(i , j+1) 
            return memo[state]
        return dp(0, 0)