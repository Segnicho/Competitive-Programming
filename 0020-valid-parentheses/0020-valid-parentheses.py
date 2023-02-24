class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(','{', '[']
        closes = [')','}', ']']
        stack = []
        for par in s:
            if par in opens:
                stack.append(par)
            elif stack and closes.index(par) == opens.index(stack[-1]):
                stack.pop()
            else:
                return False
        return not stack