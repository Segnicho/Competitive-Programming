class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        mx = sum(weights)
        mn = max(weights)
        
        def daysNeeded(weights, md):
            dNeeded = 1
            curr = 0
            for weight in weights:
                if curr + weight > md:
                    curr = 0
                    dNeeded += 1
                curr += weight
            return dNeeded
        
        while mn < mx:
            md = (mn+mx)//2
            req = daysNeeded(weights, md) 
            if  req > days:
                mn = md + 1
            else:
                mx = md 
        return mn