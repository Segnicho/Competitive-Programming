class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        res = 0
        n = len(word)
        for i, c in enumerate(word):
            if c in vowels:
                res += (n-i-1)*(i+1) + (i + 1)
        
        return res