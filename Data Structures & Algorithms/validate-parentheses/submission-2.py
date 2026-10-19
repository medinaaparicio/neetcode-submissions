class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'(':')', '[':']', '{':'}'}
        opening = "([{"
        closing = "}])"
        stack = []

        for char in s: 
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or parens[stack.pop()] != char:
                    return False
            else: return False
        if len(stack) != 0: return False 
        return True
