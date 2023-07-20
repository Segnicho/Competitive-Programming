class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        visited = set()
        for num in nums:
            
            for v in visited:
                difference = num-v
                if (difference,v) in mp:
                    longest = mp[difference,v] + 1
                else:
                    longest = 2
                mp[difference,num] = max(mp[difference,num],longest)
            if num not in visited:
                mp[0,num] = 1
            visited.add(num)

        return max(mp.values()) 