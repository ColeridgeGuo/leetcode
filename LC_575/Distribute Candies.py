"""
Given an integer array with even length, where different numbers in this array
represent different kinds of candies. Each number means one candy of the
corresponding kind. You need to distribute these candies equally in number to
brother and sister.
Return the maximum number of kinds of candies the sister could gain.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return min(len(candies) // 2, len(set(candies)))


def main():
    while True:
        try:
            line = input()
            candies = stringToList(line)

            sol = Solution()
            ret = sol.distributeCandies(candies)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
