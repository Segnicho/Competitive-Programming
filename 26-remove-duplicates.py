class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] > nums[holder] and holder<= seeker:
                holder += 1
                nums[holder] = nums[seeker]
            seeker+=1
        holder+=1
        return holder
