class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                difference = i - coin
                if difference < 0:
                    break
                dp[i] = min(dp[i], 1+dp[difference])
        
        
        return dp[amount] if dp[amount] < float('inf') else -1
        # Let C be the number of coins and A be the amount.
        # Time Complexity: O(C * Amount)
        # Space Complexity: O(Amount)
        
solution = Solution()
print(solution.coinChange([1,2,5], 11))