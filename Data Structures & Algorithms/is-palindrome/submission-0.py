class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = '' # filtering out the non-abcs and turning them all into lowercase
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]