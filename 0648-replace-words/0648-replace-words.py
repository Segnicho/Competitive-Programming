class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        arr = sentence.split(" ")
        for i,word in enumerate(arr):
            root = trie.findRoot(word)
            if root:
                arr[i] = root
        return " ".join(arr)
        
        
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
        

    def findRoot(self, word: str) -> bool:
        curr = self.root
        res = ""
        for ch in word:
            if not ch in  curr.children:
                return ""
            elif curr.children[ch].isEnd:
                return res + ch
            res += ch
            curr = curr.children[ch]
        return res
