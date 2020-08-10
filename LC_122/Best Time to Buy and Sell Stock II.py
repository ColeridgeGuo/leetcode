"""
    Say you have an array prices for which the ith element is the price of a
    given stock on day i.
    
    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (i.e., buy one and sell one share of the stock
    multiple times).
    
    Note: You may not engage in multiple transactions at the same time (i.e.,
    you must sell the stock before you buy again).
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Time complexity : O(n). Single pass.
            Space complexity: O(1). Constant space needed.
        """
        max_profit = 0
        for day in range(1, len(prices)):
            if prices[day] > prices[day-1]:
                max_profit += prices[day] - prices[day-1]
        return max_profit


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
