class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        res = 0
        for word in words:
            trie.insert(word)
        dkt = defaultdict(list)
        for i, c in enumerate(s):
            dkt[c].append(i)
        
        def helper(curr, i):
            nonlocal res
            if i > len(s):
                return
            for n in curr.children:
                idx = bisect_left(dkt[n], i)
                if idx < len(dkt[n]):
                    res += curr.children[n].isEnd
                    helper(curr.children[n] , dkt[n][idx]+1)
        helper(trie.root, 0)
        return res
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
            curr = curr.children[ch]
        curr.isEnd += 1
    
                    