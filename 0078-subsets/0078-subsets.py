class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def BT(i, temp):
            if i >= n:
                res.append(temp[:])
                return 
            temp.append(nums[i])
            BT(i+1, temp)
            temp.pop()
            BT(i+1, temp)
        BT(0, [])
        return res