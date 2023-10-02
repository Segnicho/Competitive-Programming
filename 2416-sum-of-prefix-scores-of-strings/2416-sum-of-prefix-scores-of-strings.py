class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        trie = Trie()
        
        for word in words:
            trie.insert(word)

        for word in words:
            score =trie.getCount(word)
            res.append(score)
        return res
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd =False
        self.count = 0 
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr.children[c].count += 1
            curr = curr.children[c]
        curr.isEnd = True
        
    def getCount(self, word):
        curr = self.root
        res = 0
        for c in word:
            res += curr.children[c].count
            curr = curr.children[c]
        return res    