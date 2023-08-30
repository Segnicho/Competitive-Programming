class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def calcDaysNeeded(md):
            needed = 1
            curr = 0
            for i, weight in enumerate(weights):
                if curr + weight > md:
                    curr = 0
                    needed += 1
                curr += weight
            return needed
        
        mn, mx = max(weights), sum(weights)
        while mn < mx:
            md = (mn + mx) //2
            daysNeeded = calcDaysNeeded(md)
            if daysNeeded > days:
                mn = md + 1
            else:
                mx =   md
        return mn
                
                