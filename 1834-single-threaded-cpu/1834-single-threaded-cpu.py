class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        res = []
        for i, num in enumerate(tasks):
            num.append(i)
        tasks.sort(reverse=True)
        time = 0
        while tasks:
            # handle those that can be handled directly as they came and time suits
            start, t, idx = tasks.pop()
            while heap and  start > time:
                ct, cidx = heappop(heap)
                res.append(cidx)
                time += ct
            heappush(heap, [t, idx])
            time = max(time, start)
        # handle those which are left from the first process
        while heap:
            t, idx = heappop(heap)
            res.append(idx)
        return res
    