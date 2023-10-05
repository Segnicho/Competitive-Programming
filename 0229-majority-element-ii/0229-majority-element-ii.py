class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        count = Counter(nums)
        k = n//3
        res = []
        
        for key, value in count.items():
            if value > k:
                res.append(key)
            
        return res
        