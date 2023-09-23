class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        n = len(s)
        def isPalindrome(string):
            i, j = 0, len(string)-1
            while i <= j:
                if string[i] != string[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def dfs(i):
            if i == n:
                res.append(curr[:])
                return 
            for j in range(i, n):
                if isPalindrome(s[i:j+1]):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()
        dfs(0)
        return res