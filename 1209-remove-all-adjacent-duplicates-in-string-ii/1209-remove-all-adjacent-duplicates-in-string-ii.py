class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = [[s[0], 1]]
        for i in range(1, n):
            c = s[i]
            if not stack:
                stack.append([c, 1])
            else:
                top = stack[-1][0]

                if c == top:
                    if stack[-1][-1] == k-1:
                        stack.pop()
                    else:
                        stack[-1][-1] += 1
                else:
                    stack.append([c, 1])

        return "".join([s[0]*s[1] for s in stack]) if stack else ""
    