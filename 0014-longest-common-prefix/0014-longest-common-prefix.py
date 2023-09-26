
class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0
        self.res = 0
    def insterToTrie(self, word):
        curr = self.root
        for c in word:
            if not curr.children[ord(c)-ord("a")]:
                newNode  = TrieNode()
                curr.children[ord(c)-ord("a")] = newNode
            curr.count += 1
            self.res = max(self.res, curr.count)
            curr = curr.children[ord(c)-ord("a")]
    
    def getPrefixLength(self):
        res = ""
        curr = self.root
        while curr:
            cnt = 0
            ptr = 0
            for i in range(26):
                if curr.children[i]:
                    cnt += 1
                    ptr = i
            if cnt == 1:
                res += chr(ord("a")+ptr)
            else:
                break
            curr = curr.children[ptr]
        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        res = "a"*201
        for word in strs:
            if not word: return ""
            if len(word)<len(res):
                res = word
            trie.insterToTrie(word)
        ans = trie.getPrefixLength()
        return res if len(res) < len(ans) else ans
            