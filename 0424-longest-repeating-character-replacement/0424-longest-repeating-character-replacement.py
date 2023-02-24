class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = Counter()
        left = 0
        maxLen = 0
        largest = 1
        for right in range(len(s)):
            mp[s[right]] = mp[s[right]] + 1
            largest = max(largest, mp[s[right]])
            if largest + k >= right - left + 1:
                maxLen = max(maxLen, right - left + 1)
            if largest + k < right - left + 1:
                mp[s[left]] -= 1
                left += 1
        return maxLen
        