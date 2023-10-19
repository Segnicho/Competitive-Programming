class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        i = 2

        
        while i**2 <= n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
            
        return sum(is_prime)
    