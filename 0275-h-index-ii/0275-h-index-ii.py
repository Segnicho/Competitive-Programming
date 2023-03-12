class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        res = float("inf")
        while left <= right:
            mid = left + (right -left) // 2
            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        if res == float("inf"):
            return 0
        res = len(citations) - res
        return res