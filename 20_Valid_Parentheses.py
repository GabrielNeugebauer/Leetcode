class Solution:
    def isValid(self, s: str) -> bool:
        #24ms and 16.69MB, O(N)
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack.pop() != char:
                return False
        return not stack