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
                    
        # self.n = len(self.words)
        # self.prefTrie = Trie()
        # self.suffTrie = Trie()
        # for i, word in  enumerate(self.words):
        #     self.prefTrie.insert(word, i)
        #     r = word[::-1]
        #     self.suffTrie.insert(r, i)
        
    def f(self, pref: str, suff: str) -> int:
        # print(self.dkt)
        q = pref+ "*"+ suff
        if q in self.dkt:
            return self.dkt[q]
        else:
            return -1
        
        # if  self.prefTrie.startsWith(pref) and self.suffTrie.startsWith(suff[::-1]):
        #     pre =  self.prefTrie.findIndex(pref)
        #     suf =  self.suffTrie.findIndex(suff[::-1])
        #     # return 0
        #     for num in (pre[-1][::-1]):
        #         if num in suf[0]:
        #             return num
        # else:
        #     return -1
                        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.idx = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str, i) -> None:
        curr = self.root
        for ch in word:
            if  not ch in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
            curr.children[ch].idx.append(i)
            curr = curr.children[ch]
        curr.isEnd = True
    def findIndex(self, pref):
        curr = self.root
        for ch in pref:
            # if ch not in curr.children:
            curr = curr.children[ch]
        return [set(curr.idx), curr.idx]
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not c in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr and curr.isEnd
    

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not ch in  curr.children:
                return False
            curr = curr.children[ch]
        return True
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)