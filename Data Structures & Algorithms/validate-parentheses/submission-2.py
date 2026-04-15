class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_opening = {'[':']', '{':'}', '(':')'}

        for bracket in s:
            if bracket in valid_opening:
                stack.append(bracket)
            else:
                if not stack or bracket != valid_opening[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False