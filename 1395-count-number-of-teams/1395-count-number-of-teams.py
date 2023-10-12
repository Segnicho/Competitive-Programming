class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for i, num in enumerate(rating):
            
            lless = rmore = lmore =rless = 0
            
            for lft in rating[:i+1]:
                if lft < num:
                    lless += 1
                elif lft > num:
                    lmore += 1
            for right in rating[i+1:]:
                if num < right:
                    rmore += 1
                elif num > right:
                    rless += 1
            res += lless*rmore + lmore*rless
        return res
            