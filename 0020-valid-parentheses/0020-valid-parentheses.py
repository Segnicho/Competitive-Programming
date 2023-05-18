class Solution:
    def isValid(self, s: str) -> bool:
        combo = {")" : "(", "]": "[", "}": "{"}
        stack = []
        for token in s:
            if token in combo.values():
                stack.append(token)
            elif stack and combo[token] ==  stack[-1]:
                stack.pop()
            else:
                return False
        return not stack and len(s)> 1