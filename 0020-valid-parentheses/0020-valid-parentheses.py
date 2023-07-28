class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"]": "[",")": "(","}" : "{" }
        stack = []
        for token in s:
            if token not in mp:
                stack.append(token)
            elif stack and mp[token] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack