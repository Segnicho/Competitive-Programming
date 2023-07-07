class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        heap = [1]
        visited = set()
        while n:
            num = heappop(heap)
            for prime in primes:
                res = prime*num
                if res not in visited:
                    heappush(heap, res)
                    visited.add(res)
            n-=1
        return num
    