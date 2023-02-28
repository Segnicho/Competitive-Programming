class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {     "+",
                      "-",
                      "*", 
                      "/"
               }
        
        stack = []
        for token in tokens:
            if token in ops:
                num2 = eval(stack.pop())
                num1 = eval(stack.pop())
                if token == "+":
                    stack.append(str(num1 + num2))
                elif token == "-":
                    stack.append(str(num1 - num2))
                elif token == "*":
                    stack.append(str(num1 * num2))
                elif token == "/":
                    stack.append(str(int(num1 / num2)))
            else:
                stack.append(token)
        return eval(stack[0])