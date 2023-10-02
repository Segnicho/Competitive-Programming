class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.dkt = defaultdict()

    def insert(self, key: str, val: int) -> None:
        prev = 0
        if key in self.dkt:
            prev = self.dkt[key]
        self.dkt[key] = val
        self.trie.insert(key, val, prev)
        

    def sum(self, prefix: str) -> int:
        res = self.trie.findSum(prefix)
        return int( res/len(prefix))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str, cnt, prev) -> None:
        curr = self.root
        exists = self.search(word)
        for ch in word:
            if  not ch in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
            curr.children[ch].count = curr.children[ch].count + cnt - prev
            curr = curr.children[ch]
        curr.isEnd = True
    def findSum(self, pref):
        curr = self.root
        res = 0
        for c in pref:
            if c in curr.children:
                res = curr.children[c].count
                curr = curr.children[c]
            else:
                return 0
            
        return res*len(pref)
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not c in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr and curr.isEnd

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)