class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        res = -float("inf")
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            res = max(right-left+1, res)
            st.add(s[right])
        return res if res != -float("inf") else 0
                
            