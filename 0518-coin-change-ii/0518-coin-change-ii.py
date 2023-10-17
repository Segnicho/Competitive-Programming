class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(i, target = amount):
            if i == 0:
                return 1 if target % coins[i] == 0 else 0
            nonTaken = dp(i-1, target)
            taken = 0
            if coins[i] <= target:
                taken = dp(i, target-coins[i])
            return taken + nonTaken
                
        n = len(coins)
        return dp(n-1)