class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0
        m = 0

        for R in range(1, len(prices)):
            if prices[L] < prices[R]:
                m = max(prices[R] - prices[L], m)
            else:
                L = R
            
            R += 1

        return m

