class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {')':'(', '}':'{', ']':'['}

        for paren in s:
            if paren in parens.values():
                stack.append(paren)
            else:
                if stack and stack[-1] == parens.get(paren):
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        
        return False
