class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        mp = defaultdict()
        curr = 0
        for i in range(1,1000):
            mp[i] = curr
            if curr < len(days) and i >= days[curr]:
                curr += 1
        @cache
        def dp(i):
            if i >= n:
                return 0
            return min(costs[0] + dp(i+1), costs[1] + dp(mp[days[i]+7]), costs[2] + dp(mp[days[i]+30]) )
        return dp(0)