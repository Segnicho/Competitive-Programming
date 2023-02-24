class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for right in range(len(logs)):
            if stack and logs[right] =="../":
                stack.pop()
            elif logs[right] =='./' or (not stack and logs[right]  == "../") :
                continue
            else:
                stack.append(logs[right])
        return len(stack)