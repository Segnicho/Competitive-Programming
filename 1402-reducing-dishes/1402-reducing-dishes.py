class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        total_satisfaction = max_satisfaction = 0
        n = len(satisfaction)
        i = 0
        while i<n and satisfaction[i] + total_satisfaction > 0:
                total_satisfaction += satisfaction[i]
                max_satisfaction += total_satisfaction
                i+= 1
        return max_satisfaction