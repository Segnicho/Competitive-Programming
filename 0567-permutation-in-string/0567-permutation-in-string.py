class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count  = Counter(s1)
        s2count  = Counter()
        for right in range(len(s1)):
            if right < len(s2):
                s2count[s2[right]] += 1
        left = 0
        for r in range(right+1, len(s2)):
            if s1count == s2count:
                return True
            s2count[s2[left]] -= 1
            s2count[s2[r]] += 1
            left+=1
        return s1count == s2count