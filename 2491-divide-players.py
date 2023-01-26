class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0 
        right = len(skill)-1
        sm = skill[0] + skill[-1]
        total = 0
        while left<right:
            curr_chemistry = skill[left] * skill[right]
            curr_sm =  skill[left] + skill[right]
            if curr_sm != sm:
                return -1
            total+=curr_chemistry
            left+=1
            right -= 1
        return total
