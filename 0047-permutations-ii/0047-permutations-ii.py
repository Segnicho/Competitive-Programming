class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(arr,temp ):
            if not arr:
                res.append(temp[:])
            ans = set()
            for num in arr:
                if num not in ans:
                    ans.add(num)
                    temp.append(num)
                    otherNums = arr[:]
                    otherNums.remove(num)                
                    backTrack(otherNums, temp)
                    temp.pop()
        nums.sort()
        backTrack(nums, [])
        return res
    