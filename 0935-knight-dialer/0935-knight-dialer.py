class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        def inbound(x, y):
            nums = 0<=x<3 and 0 <= y < 3
            return nums or (x, y) == (3, 1)
        
        directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2] , [1, -2]]
        def dp(i,j, jump):
            if jump == 0:
                return 1
            ans = 0
            if (i, j, jump) in memo:
                return memo[(i, j, jump)]
            for x, y in directions:
                row, col = i+x, y+j
                if inbound(row, col):
                    ans += dp(row, col, jump-1)
            memo[(i, j, jump)] =  ans % mod
            return memo[(i, j, jump)] 

        res = 0
        memo = {}
        for i in range(4):
            for j in range(3):
                if inbound(i, j):
                    res += dp(i, j, n-1)
        return res % mod