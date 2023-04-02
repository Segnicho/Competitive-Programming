class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors =  set()
        for num in nums:
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factors.add(d)
                    num //= d
                d += 1
            if num > 1:
                factors.add(num)
        return len(factors)
        
        