"""
Given coin denominations and an integer k, return the kth smallest positive
amount that is divisible by at least one denomination.
"""
from math import lcm
from typing import List

from common_funcs import stringToList


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        """
        Use inclusion-exclusion to count how many distinct valid amounts are at
        most x, then binary-search for the smallest x whose count reaches k.

        Time Complexity: O(n * 2^n + 2^n * log(min(coins) * k))
        Space Complexity: O(2^n)
        """
        n = len(coins)
        terms = []

        # Each subset contributes multiples of its LCM. Odd-sized subsets are
        # added and even-sized subsets are subtracted by inclusion-exclusion.
        for mask in range(1, 1 << n):
            common = 1
            selected = 0

            for i, coin in enumerate(coins):
                if mask & (1 << i):
                    common = lcm(common, coin)
                    selected += 1

            sign = 1 if selected % 2 == 1 else -1
            terms.append((common, sign))

        def count_amounts(x: int) -> int:
            total = 0
            for common, sign in terms:
                total += sign * (x // common)
            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2
            if count_amounts(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    while True:
        try:
            line = input()
            coins = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.findKthSmallest(coins, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
