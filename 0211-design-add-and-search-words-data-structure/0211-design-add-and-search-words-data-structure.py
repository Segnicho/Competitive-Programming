
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if  not ch in curr.children:
                nwNode = TrieNode()
                curr.children[ch] = nwNode
            curr = curr.children[ch]
        curr.isEnd = True
    def search(self, word: str) -> bool:
        curr = self.root
        def helper(node, i):
            if i >= len(word) :
                return node.isEnd
            elif word[i] in node.children:
                if word[i] in node.children:
                    node = node.children[word[i]]
                    return helper(node, i+1)
            elif word[i] == ".":
                for c in node.children:
                    if helper(node.children[c], i+1):
                            return True
                return False
            else:
                return False        
        return helper(curr, 0)
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        