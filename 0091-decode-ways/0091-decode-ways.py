class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            res = dp(i + 1)
            if i + 1 < len(s) and int(s[i : i + 2]) < 27:
                    res += dp(i + 2)
            return res
        return dp(0)
        
        