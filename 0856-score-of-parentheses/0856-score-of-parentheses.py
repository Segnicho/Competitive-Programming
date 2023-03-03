class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack =  []
        res = 0
        for token in s:
            if token == '(':
                stack.append(res)
                res = 0
            else:
                val =  stack.pop()
                rs = max(res, 1)
                res += (val + rs)
        return res