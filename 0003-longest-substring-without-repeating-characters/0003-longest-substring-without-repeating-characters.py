class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            res = max(res, right-left + 1)
            st.add(s[right])
        return res
    