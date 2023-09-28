class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m , n = len(str1), len(str2)
        dp = [["" for i in range(n+1)] for j in range(m+1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1], key=len)
        longestCS = dp[-1][-1]
        i, j, ans = 0, 0, ""
        for ch in longestCS:
            while ch != str1[i]:
                ans += str1[i]
                i+=1
            while ch != str2[j]:
                ans += str2[j]
                j += 1
            ans += ch
            i, j = i + 1, j + 1

        ans += str1[i:]
        ans += str2[j:]
            
        return ans