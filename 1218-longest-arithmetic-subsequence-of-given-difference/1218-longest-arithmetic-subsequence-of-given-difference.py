class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        res = 0
        for num  in arr:
            dp[num]  = dp[num-difference] + 1
            res = max(dp[num], res)
        return res
    