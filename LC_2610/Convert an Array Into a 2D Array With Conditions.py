"""
You are given an integer array nums. You need to create a 2D array from nums
satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.
"""
import collections
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Count frequencies of each num first, then construct the matrix using
        numbers with positive frequencies.
        """
        counter = collections.Counter(nums)
        ans = []
        while counter:
            row = [num for num in counter]
            counter -= collections.Counter(row)
            ans.append(row)
        return ans

    def findMatrix_2(self, nums: List[int]) -> List[List[int]]:
        """
        Initialize with an empty Counter.
        Frequency of the number >= len(ans) means that we need another row for
        this number because it has already appeared in the previous row. We then
        add it to the new row and increment the frequency.
        """
        counter = collections.Counter()
        ans = []
        for num in nums:
            if counter[num] >= len(ans):
                ans.append([])
            ans[counter[num]].append(num)
            counter[num] += 1
        return ans


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.findMatrix(nums)
            ret2 = sol.findMatrix_2(nums)

            out = listToString(ret)
            out2 = listToString(ret2)
            print(f"Solved by counting frequencies first:     {out}")
            print(f"Solved by constructing matrix on the fly: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
