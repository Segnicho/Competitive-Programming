class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:(x[0]))
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            last = res[-1][-1]
            if intervals[i][0] <= last:
                res[-1][1] = max(last, intervals[i][1])
            else:
                res.append(intervals[i])
        return res
    