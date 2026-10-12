class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for i in s:
            if stack and stack[-1]==mapping.get(i):
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True