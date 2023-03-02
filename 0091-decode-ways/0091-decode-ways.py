class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dp(i + 1)
            if i + 1 < len(s):
                if int(s[i : i + 2]) < 27:
                    res += dp(i + 2)
            return res
        # return dp(0)
        
        dp = [0] * (len(s) + 1)
        for i in range(len(dp) - 1,-1,-1):
            if i == len(s):
                dp[i] =  1
            elif s[i] == "0":
                dp[i] = 0
            else:
                res = dp[i + 1]
                if i + 1 < len(s):
                    if int(s[i : i + 2]) < 27:
                        res += dp[i + 2]
                dp[i] = res
        return dp[0]