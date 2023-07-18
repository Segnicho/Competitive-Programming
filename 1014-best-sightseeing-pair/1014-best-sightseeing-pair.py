class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = cur = 0
        for num in values:
            res = max(res, cur+num)
            cur = max(num, cur) - 1
        return res