class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for _ in range(right+1)]
        is_prime[0] = is_prime[1] = False
        
        ans = []
        res = []
        
        i = 2
        while i * i <= right:
            if is_prime[i]:
                j = i * i
                while j <= right:
                    is_prime[j] = False
                    j += i
            i += 1
        
        for i, num in enumerate(is_prime):
            if num and (i >= left and i <= right):
                res.append(i)
        
        if not res or len(res) < 2:
            return [-1,-1 ]
        mn = float("inf")
        for i in range(1, len(res)):
            if res[i] - res[i-1] < mn :
                ans = []
                ans.append(res[i-1])
                ans.append(res[i])
                mn = res[i] - res[i-1]
        return  ans
    