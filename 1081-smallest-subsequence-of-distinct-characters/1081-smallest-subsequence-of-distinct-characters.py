class Solution:
    def smallestSubsequence(self, s: str) -> str:
        occuredAt = {}
        st = set()
        stack = []
        for i, char in enumerate(s):
            occuredAt[char] = i
        
        for i, char in enumerate(s):
            if char not in st:
                while stack and ord(stack[-1]) > ord(char) and occuredAt[stack[-1]]>i:
                    st.remove(stack[-1])
                    stack.pop()
                
                st.add(char)
                stack.append(char)
        return "".join(stack)