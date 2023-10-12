class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        num =  math.factorial(2*n)
        expo = pow(2, n)
        return (num//expo) % mod
    