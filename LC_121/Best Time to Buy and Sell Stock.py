"""
You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            res = max(res, prices[i] - lowest)
        return res

    def maxProfit_kadane(self, prices: List[int]) -> int:
        res = 0
        curr_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            curr_profit = max(0, curr_profit + diff)
            res = max(res, curr_profit)
        return res

def main():
    while True:
        try:
            line = input()
            prices = stringToList(line)

            sol = Solution()
            ret = sol.maxProfit(prices)
            ret2 = sol.maxProfit_kadane(prices)

            print(f"Solved with finding lowest price to buy: {ret}")
            print(f"Solved with Kadane's algorithm:          {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
