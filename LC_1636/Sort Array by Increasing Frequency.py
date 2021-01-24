"""
Given an array of integers nums, sort the array in increasing order based on the
frequency of the values. If multiple values have the same frequency, sort them
in decreasing order.

Return the sorted array.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        Count the frequency of each number, then sort nums first by frequency,
        then reversely by value
        """
        from collections import Counter
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.frequencySort(nums)
            
            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
