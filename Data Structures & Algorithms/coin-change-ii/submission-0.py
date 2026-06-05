class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Step 1: Initialize the DP array with zeros.
        # Its size is amount + 1 so we can index from 0 to amount.
        dp = [0] * (amount + 1)
        
        # Step 2: Base Case.
        # There is exactly 1 way to make an amount of 0: by choosing no coins.
        dp[0] = 1
        
        # Step 3: Loop through each coin option
        for coin in coins:
            # Loop forward from the current coin's value up to the target amount
            for w in range(coin, amount + 1):
                # The new ways to make amount 'w' is the current ways
                # plus the ways to make the remaining amount (w - coin)
                dp[w] += dp[w - coin]
                
        return dp[amount]