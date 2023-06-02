class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        uniques = [nums[0]]
        count = Counter(nums)
        for i in range(1,n):
            if nums[i] > uniques[-1]:
                uniques.append(nums[i])
        m = len(uniques)
        @cache
        def dp(i):
            if i >= m:
                return 0
            if i+1 < m and uniques[i+1] == uniques[i] + 1:
                return max(count[uniques[i]]*uniques[i]+ dp(i+2), dp(i+1))
            return count[uniques[i]]*uniques[i] +  dp(i+1) 
        return dp(0)