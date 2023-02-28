class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = { "+","-","*", "/" }
        
        stack = []
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                val = eval(num1 + token + num2)
                stack.append(str(int(val)))
            else:
                stack.append(token)
        return int(stack[0])