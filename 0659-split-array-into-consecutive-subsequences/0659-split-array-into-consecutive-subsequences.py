class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        count = Counter(nums)
        heap = []
        
        if len(nums) <= 2:
            return False
        
        last = Counter()
        for num in nums:
            if count[num]:
                if last[num-1]:
                    last[num-1] -= 1
                    last[num] += 1
                elif count[num+1] and count[num+2]:
                    last[num+2] += 1
                    count[num+1] -= 1
                    count[num+2] -= 1
                else:
                    return False
                count[num] -= 1
        return True