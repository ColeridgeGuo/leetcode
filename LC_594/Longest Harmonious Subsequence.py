"""
We define a harmonious array as an array where the difference between its
maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest
harmonious subsequence among all its possible subsequences.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        from collections import Counter
        c = Counter(nums)
        lhs = 0
        for num in c:
            if num + 1 in c:
                lhs = max(lhs, c.get(num, 0) + c[num + 1])
        return lhs


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.findLHS(nums)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
