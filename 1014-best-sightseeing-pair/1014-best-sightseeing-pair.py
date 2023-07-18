class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = float("-inf")
        left = values[0]
        for i in range(1, len(values)):
            res = max(res,left + values[i] - i )
            left = max(left, values[i] + i)
        return res