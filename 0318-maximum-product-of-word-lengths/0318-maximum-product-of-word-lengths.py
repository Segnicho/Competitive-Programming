class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        arr = []
        for word in words:
            letters = set()
            for letter in word:
                letters.add(letter)
            arr.append(letters)
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[i] & arr[j]:
                    continue
                res = max(res, len(words[i]) * len(words[j]))
        return res