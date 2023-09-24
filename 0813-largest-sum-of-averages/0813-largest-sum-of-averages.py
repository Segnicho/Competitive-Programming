class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def helper(index, k):
            if index == n:
                return 0

            if dp[index][k] != -1:
                return dp[index][k]

            if k == 1:
                _sum = 0
                for i in range(index, n):
                    _sum += nums[i]
                return _sum / (n - index)

            maxi = 0
            curr_avg = 0

            for i in range(index, n - k + 1):
                curr_avg += nums[i]
                maxi = max(maxi, (curr_avg / (i - index + 1)) + helper(i + 1, k - 1))

            dp[index][k] = maxi
            return maxi

        return helper(0, k)
