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


def main():
    while True:
        try:
            line = input()
            prices = stringToList(line)

            ret = Solution().maxProfit(prices)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
