class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque()
        coins.sort(reverse = True)
        dikt = defaultdict(int)
        for num in coins:
            if amount - num >=0:
                q.append((amount- num, 1))
                dikt[amount- num] = 1

        while q:
            leftCoins, step = q.popleft()
            if leftCoins == 0:
                return step
            for i, num in enumerate(coins):
                if leftCoins -num >= 0 and leftCoins-num not in dikt:
                    q.append((leftCoins - num, step+1))
                    dikt[leftCoins-num] = step+1
        
        return -1
                