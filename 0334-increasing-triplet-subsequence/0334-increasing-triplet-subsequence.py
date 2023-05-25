class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest =  secSmallest = float("inf")
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= secSmallest:
                secSmallest = num
            else:
                return True
        return False