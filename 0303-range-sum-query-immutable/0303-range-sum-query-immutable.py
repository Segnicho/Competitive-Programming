class NumArray:

    def __init__(self, nums: List[int]):
        self.prefSum = [0]
        for num in nums:
            self.prefSum.append(num+self.prefSum[-1])

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefSum[left]
        rightSum = self.prefSum[right+1]
        return rightSum-leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right) 