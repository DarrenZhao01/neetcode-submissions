class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        mem = [0] * (n + 1)
        mem[1], mem[2] = 1, 2

        for i in range(3, n + 1):
            mem[i] = mem[i - 1] + mem[i - 2]
        
        return mem[n]
