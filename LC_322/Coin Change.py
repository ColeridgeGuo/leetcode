"""
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def coinChange_backtrack(self, coins: List[int], amount: int) -> int:
        ans = float('inf')
        total = 0
        
        def backtrack(numCoins):
            nonlocal ans, total
            if total == amount:
                ans = min(ans, numCoins)
                return
            if total > amount:
                return
            for denom in coins:
                total += denom
                backtrack(numCoins + 1)
                total -= denom
                
        backtrack(0)
        return ans if ans != float('inf') else -1
    
    def coinChange_backtrack2(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        count = [0] * (amount + 1)
        
        def backtrack(remain):
            nonlocal count
            if remain < 0:
                return -1
            if remain == 0:
                return 0
            if count[remain] != 0:
                return count[remain]
            min_coins = float('inf')
            for coin in coins:
                res = backtrack(remain - coin)
                if 0 <= res < min_coins:
                    min_coins = res + 1
            count[remain] = -1 if min_coins == float('inf') else min_coins
            return count[remain]
        
        return backtrack(amount)
    
    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        """
        Time Complexity: O(A*c), where A = amount, c = len(coins)
        Space Complexity: O(A)
        dp[i] = the least number of coins to form i amount
        """
        dp = [0] + [amount + 1] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
    
    def coinChange_dp2(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1


def main():
    while True:
        try:
            line = input()
            coins = stringToList(line)
            line = input()
            amount = int(line)
            
            sol = Solution()
            ret = sol.coinChange_backtrack(coins, amount)
            ret2 = sol.coinChange_backtrack2(coins, amount)
            ret3 = sol.coinChange_dp(coins, amount)
            ret4 = sol.coinChange_dp2(coins, amount)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            out4 = str(ret4)
            print(f"Solved by backtracking:              {out}")
            print(f"Solved with pruning and memoization: {out2}")
            print(f"Solved with dynamic programming:     {out3}")
            print(f"Solved with dynamic programming 2:   {out4}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
