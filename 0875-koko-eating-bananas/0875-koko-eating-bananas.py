class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mn = 1
        mx = max(piles)
        ans = 1
        while mx >= mn:
            md = (mn+mx)//2
            time = 0
            for pile in piles:
                if pile % md == 0:
                    time += pile // md
                else:
                    time += (pile//md)+1
            if time > h:
                mn = md + 1
            else:
                ans = md
                mx = md - 1
        return ans