class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = set()
        stack = []
        occuredLast = {}
        for i, char in enumerate(s):
            occuredLast[char] = i
        for i, char in enumerate(s):
            if char not in st:
                while stack and occuredLast[stack[-1]] > i and ord(char) < ord(stack[-1]):
                    st.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                st.add(char)
        return "".join(stack)