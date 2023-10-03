class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        @cache
        def helper(i):
            if i >= n:
                return True
            for j in range(i, n+1):
                if trie.search(s[i:j]):                    
                    if helper(j):
                        return True
                
        return helper(0)
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if  not ch in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
            curr = curr.children[ch]
        curr.isEnd = True

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
    