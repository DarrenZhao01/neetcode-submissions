class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
           
            seen.add(n)

            digits = str(n)
            sum = 0
            for digit in digits:
                sum += int(digit) * int(digit)
           
            n = sum
            
        
        return True
            