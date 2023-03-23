class Solution:
    def findScore(self, nums: List[int]) -> int:
        arr = []
        marked = set()
        res = 0
        for i,num in enumerate(nums):
            arr.append((num, i))
        
        arr.sort()
        
        for num, i in arr:
            if i not in marked:
                res += num
                marked.add(i+1)
                marked.add(i-1)
        return res