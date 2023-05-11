class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        res = []
        time = 0
        for idx, task in enumerate(tasks):
            task.append(idx)
        tasks.sort(reverse = True)
        index = 0
        while tasks:
            start, t, index = tasks.pop()
            while heap and  start > time:
                ct, idx = heappop(heap)
                res.append(idx)
                time += ct
            heappush(heap, [t, index])
            time = max(time, start)
        while heap:
            t, idx = heappop(heap)
            res.append(idx)
        return res
    