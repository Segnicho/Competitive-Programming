class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i, c in enumerate(haystack):
            if c != needle[0]:
                continue
            k = i
            j = 0
            while j<n and k<m and  haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == n:
                return i
        return -1
    