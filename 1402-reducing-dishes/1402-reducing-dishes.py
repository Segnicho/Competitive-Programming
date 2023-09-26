class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)
        res, curr, i = 0, 0, 0
        while i < n and curr + satisfaction[i] > 0:
            curr += satisfaction[i]
            res += curr
            i += 1
        return res