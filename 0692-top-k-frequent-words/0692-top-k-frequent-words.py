class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        count = Counter(words)
        for word, freq in count.items():
            heap.append((-freq, word))
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
