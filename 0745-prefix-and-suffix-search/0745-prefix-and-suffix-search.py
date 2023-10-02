class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.dkt = defaultdict(int)
        for k, word in enumerate(words):
            n = len(word)
            for i in range(1, n+1):
                curr = word[:i]
                for j in range(n-1, -1, -1):
                    self.dkt[curr+"*"+ word[j:]] = k
                    
    def f(self, pref: str, suff: str) -> int:
        q = pref+ "*"+ suff
        if q in self.dkt:
            return self.dkt[q]
        else:
            return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)