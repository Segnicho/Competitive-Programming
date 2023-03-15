class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, arr in enumerate(intervals):
            arr.append(i)
        sortedIntervals = sorted(intervals)
        res = []
        for start, end, idx in intervals:
            r = -1
            left = 0 
            right = len(intervals) - 1
            while left <= right:
                mid = (left + right)//2
                if sortedIntervals[mid][0] < end:
                    left = mid  + 1
                elif sortedIntervals[mid][0] >= end :
                    r = sortedIntervals[mid][-1]
                    right = mid - 1
            res.append(r)
        return res