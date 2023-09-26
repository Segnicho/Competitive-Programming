class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if  not curr.children[ord(ch) - ord("a")]:
                nwNode = TrieNode()
                curr.children[ord(ch) - ord("a")] = nwNode
            curr = curr.children[ord(ch) - ord("a")]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr =self.root
        for c in word:
            if not curr.children[ord(c)- ord("a")]:
                return False
            curr = curr.children[ord(c)- ord("a")]
        return curr and curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not curr.children[ord(ch)- ord("a")]:
                return False
            curr = curr.children[ord(ch)-ord("a")]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)