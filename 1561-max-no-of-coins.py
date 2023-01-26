class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        n = len(piles)
        k = n//3
        j = 0
        for i in range(n-2 , 0 , -2):
            j+=1
            res+=piles[i]
            if j == k:
                break
        return res
