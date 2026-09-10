"""
Given an unsorted array of integers, return the length of its longest
consecutive elements sequence.
"""
from typing import List

from common_funcs import stringToList


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0

        for number in number_set:
            if number - 1 not in number_set:
                current = number
                length = 1

                while current + 1 in number_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.longestConsecutive(nums)

            out = str(ret)
            print(out)
        except EOFError:
            break


if __name__ == '__main__':
    main()
