class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {"}": "{", ")": "(", "]": "["}

        for char in s:
            if char not in paren_map:
                stack.append(char)
                continue
            if not stack or stack[-1] != paren_map[char]:
                return False
            stack.pop()

        # If stack is empty, then all parentheses are matched
        return not stack
