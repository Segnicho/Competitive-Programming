class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = {"a","A", "E", "I", "O", "U", "e", "i", "o", "u"}
        left = 0
        right = n-1
        arr = [el for el in s]
        s = arr
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] not in vowels:
                right -= 1
            elif s[left] not in vowels and s[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        
        return "".join(s)
         