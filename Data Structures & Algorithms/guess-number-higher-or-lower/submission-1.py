# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        midpoint = (1 + n) // 2
        l = 0
        r = n
        response = guess(midpoint)
        while l <= r:
            if response == 0:
                return midpoint
            elif response == -1:
                r = midpoint - 1
            elif response == 1:
                l = midpoint + 1

            midpoint = (l + r) // 2
            response = guess(midpoint)