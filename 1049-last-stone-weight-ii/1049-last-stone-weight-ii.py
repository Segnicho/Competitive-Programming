class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot = sum(stones)
        n = len(stones)
        target = ceil(tot/2)

        def dp(s, i):
            if  s >= target or i == n:
                left = tot-s
                return abs(s-(left))
            if (s, i) not in memo:
                memo[(s, i)] = min(dp(s, i+1), dp(s+stones[i], i+1))
            return memo[(s, i)]
        memo = {}
        return dp(0, 0)

