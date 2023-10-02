class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        scoreAge = [[scores[i], ages[i]] for i in range(n)]
        scoreAge.sort()
        dp = scores[:]
        dp.sort()
        
        for i in range(n):
            for j in range(i):
                if scoreAge[j][1] <= scoreAge[i][1]:
                    dp[i] = max(dp[i], dp[j]+ scoreAge[i][0])
                    
        return max(dp)