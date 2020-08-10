"""
Given an array of 2n integers, your task is to group these integers into n pairs
of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi)
for all i from 1 to n as large as possible.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n/2) = O(n)
        """
        return sum(sorted(nums)[::2])


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.arrayPairSum(nums)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
