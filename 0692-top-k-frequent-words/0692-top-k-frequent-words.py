class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        count = Counter(words)
        for word, freq in count.items():
            res.append((freq, word))
        res.sort(key=lambda r: (-r[0], r[1]))
        return [res[i][1] for i in range(k)]
