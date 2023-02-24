class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = Counter()
        stack = []
        for right in range(len(nums2)):
            while stack and nums2[right] > stack[-1]:
                dct[stack[-1]] = nums2[right]
                stack.pop()
            stack.append(nums2[right])
        
        res = []
        for num in nums1:
            if num not in dct:
                res.append(-1)
            else:
                res.append(dct[num])
        return res
        