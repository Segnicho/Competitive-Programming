class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getZword(w):
            stack = []
            for c in w:
                if c == "#":
                    stack and stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
        return getZword(s) == getZword(t)