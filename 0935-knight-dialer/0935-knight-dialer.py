class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        def inbound(x, y):
            nums = 0<=x<3 and 0 <= y < 3
            return nums or (x, y) == (3, 1)
        
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2] , [1, -2]]
        @cache
        def dp(i,j, jump):
            if jump == 0:
                return 1
            ans = 0
            for x, y in directions:
                row, col = i+x, y+j
                if inbound(row, col):
                    ans += dp(row, col, jump-1)
            return ans%mod
        res = 0
        for i in range(4):
            for j in range(3):
                if inbound(i, j):
                    res += dp(i, j, n-1)
        return res % mod
    