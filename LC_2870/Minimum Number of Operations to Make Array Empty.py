"""
You are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of
times:
1. Choose two elements with equal values and delete them from the array.
2. Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty,
or -1 if it is not possible.
"""
import collections
import math
from typing import List

from common_funcs import stringToList


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Remove as many pairs of 3 as possible, then remove in pairs of 2
        When removing in pairs of 3, there are 3 cases:
        - remainder 0: remove all in pairs of 3
        - remainder 1: 3n+1 = 3(n-1)+4 =>
            remove (n-1) pairs of 3 and two pairs of 2 (n > 0)
        - remainder 2: 3n+2 => remove n pairs of 3 and one pair of 2
        """
        ans = 0
        freq = collections.Counter(nums)
        for num in freq:
            op3, rm3 = divmod(freq[num], 3)
            if rm3 == 0:
                ans += op3
                continue
            elif rm3 == 1 and op3 > 0:
                ans += op3 - 1
                freq[num] -= (op3 - 1) * 3
            elif rm3 == 2:
                ans += op3
                freq[num] -= op3 * 3
            op2, rm2 = divmod(freq[num], 2)
            if rm2 == 0:
                ans += op2
            else:
                return -1
        return ans

    def minOperations_2(self, nums: List[int]) -> int:
        """
         1: -1
         2 = 3*0+2*1 => 1
         3 = 3*1+2*0 => 1
         4 = 3*0+2*2 => 2
         5 = 3*1+2*1 => 2
         6 = 3*2+2*0 => 2
         7 = 3*1+2*2 => 3
         8 = 3*2+2*1 => 3
         9 = 3*3+2*0 => 3
        10 = 3*2+2*3 => 4
        ...
         n = 3*n+2*m => ceil(n/3) = (n+2)//3 = (n-1)//3 + 1
        """
        freq = collections.Counter(nums)
        ans = 0
        for num in freq.values():
            if num == 1:
                return -1
            ans += math.ceil(num / 3)
        return ans


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.minOperations(nums)
            ret2 = sol.minOperations_2(nums)

            print(f"Solved by manually removing:          {ret}")
            print(f"Solved with mathematical observation: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
