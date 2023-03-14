class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for token in s:
            strn = ""
            n = ""
            if token == "]":
                while stack[-1] != "[":
                    val = stack.pop()
                    strn = val + strn
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop()
                    n = num + n
                stack.append(int(n)*strn)
            else:
                stack.append(token)
        return "".join(stack)