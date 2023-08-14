class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        res = counter[deck[0]]
        
        def gcd(a , b):
            if b == 0:
                return a
            return gcd(b, a%b)
        for num in counter.values():
            res = gcd(res, num)
        return res != 1