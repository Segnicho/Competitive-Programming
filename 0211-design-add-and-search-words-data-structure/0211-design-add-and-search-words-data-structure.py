
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

                
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def insert(self, word: str) -> None:


#     def search(self, word: str) -> bool:
#         curr = self.root
#         def helper(node, i):
#             if i >= len(word):
#                 return node.isEnd
#             if word[i] in node.children or word[i] == ".":
#                 if word[i] in node.children:
#                     node = node.children[word[i]]
#                     return helper(node, i+1) 
#                 else:
#                     for i in range(26):
#                         if node.children[i]:
#                             if helper(node.children[ord(word[i])-ord(ch)], i):
#                                 return True
#                     return False
#             else:
#                 return False
        
#         return helper(curr, i)
        
        
#     def search(self, word: str) -> bool:
#         curr = self.root
#         def helper(node, i):
#             if i >= len(word):
#                 return node.isEnd
            
            
#             if word[i] in node.children or word[i] == ".":
#                 if word[i] in node.children:
#                     node = node.children[word[i]]
#                     return helper(node, i+1) 
#                 else:
#                     for i in range(26):
#                         if node.children[i]:
#                             if helper(node.children[ord(word[i])-ord(ch)], i):
#                                 return True
#                     return False
#             else:
#                 return False
            
                
            
#         print(curr.children)
#         for ch in word:
#             if ch != ".":
#                 if not curr.children[ord(ch)- ord("a")]:
#                     return False
#                 curr = curr.children[ord(ch)-ord("a")]
#             else:
#                 for i in range(26):
#                     if curr.children[i]:
#                         self.search(char())
#                         curr = curr.children[i]
#         return True
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)