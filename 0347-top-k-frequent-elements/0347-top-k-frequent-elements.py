class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in counter.items()]
        heapify(maxHeap)
        res = []
        for i in range(k):
            num = heappop(maxHeap)
            res.append(num[-1])
        return res