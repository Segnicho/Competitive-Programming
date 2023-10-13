class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isnumeric():
            return [int(expression)]
        
        
        res = []
        for i,token in enumerate(expression):
            if token in ["-", "+", "*"]:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        if token == '+':
                            res.append(l + r)
                        elif token == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res     