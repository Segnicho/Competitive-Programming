class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        n = len(nums)
        if 0 in count:
            for _ in range(count[0]):
                nums.append(0)
        if 1 in count:
            for _ in range(count[1]):
                nums.append(1)

        if 2 in count:
            for _ in range(count[2]):
                nums.append(2)
        nums.reverse()
        for i in range(n):
            nums.pop()
        nums.reverse()
        return nums
