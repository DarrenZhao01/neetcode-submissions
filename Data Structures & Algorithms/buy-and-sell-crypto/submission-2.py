# greedy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_sell = 0

        for r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            
            max_sell = max(prices[r] - prices[l], max_sell)
        
        return max_sell

# [7,1,5,3,6,4]
#    l r

#  max_sell = 5