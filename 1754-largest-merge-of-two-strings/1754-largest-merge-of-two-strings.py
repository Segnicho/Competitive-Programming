class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                res+= word1[i]
                i+=1
            elif word1[i] < word2[j]:
                res += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    res+= word1[i]
                    i+=1
                else:
                    res += word2[j]
                    j += 1
        res += word1[i:]
        res += word2[j:]
        return res