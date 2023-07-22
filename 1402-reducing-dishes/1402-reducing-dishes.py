class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        total_satisfaction = max_satisfaction = 0
        n = len(satisfaction)
        for i in range(n):
            if satisfaction[i] > -total_satisfaction:
                total_satisfaction += satisfaction[i]
                max_satisfaction += total_satisfaction

        return max_satisfaction