class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        res = ""
        words.sort()
        for word in words:
            trie.insert(word)
                
#         def helper(i, word):
#             if i <= 0:
#                 return True
#             start = trie.startsWith(word[:i])
#             if not start:
#                 return False
#             if start and helper(i-1, word):
#                 return True
            
        for word in words:
            isValid = trie.isValid(word)
            if isValid and len(word) > len(res):
                res = word
        return res
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if  not ch in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
                curr.count = 1
            else:
                curr.count += 1
            curr = curr.children[ch]
        curr.isEnd = True
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not ch in  curr.children:
                return False
            curr = curr.children[ch]
        return True
    def isValid(self, word):
        curr = self.root
        for ch in word:
            if not curr.children[ch].isEnd:
                return False
            curr = curr.children[ch]            
        return True
# ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]