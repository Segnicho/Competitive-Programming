class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        res = 0
        dp = defaultdict(int)
        for i in range(n):
            dp[arr[i]] = dp[arr[i]-difference] + 1
            res = max(res, dp[arr[i]]) 
        return res
    