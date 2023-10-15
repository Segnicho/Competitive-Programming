class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        def backtrack(i, currstr):
            if i >= n:
                res.append(currstr)
                return 
            if s[i].isalpha():
                backtrack(i+1, currstr+s[i].upper())
                backtrack(i+1, currstr+s[i].lower())                
            else:
                backtrack(i+1, currstr+s[i])
        res = []
        backtrack(0, "")
        return res