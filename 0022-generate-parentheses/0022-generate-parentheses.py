class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        temp = []
        def bt(opn, clos):
            if opn == clos == n:
                res.append("".join(temp))
                return
            if opn < n:
                temp.append("(")
                bt(opn+1, clos)
                temp.pop()
            if clos < opn:
                temp.append(")")
                bt(opn, clos+1)
                temp.pop()
        res = []
        bt(0, 0)
        return res
                