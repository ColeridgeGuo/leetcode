"""
Given an integer array nums of unique elements, return all possible subsets 
(the power set). The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""
from typing import List
from common_funcs import listToString, stringToList


class Solution:
    def subsets_py(self, nums: List[int]) -> List[List[int]]:
        from itertools import chain, combinations
        return list(chain.from_iterable(combinations(nums, n)
                                        for n in range(len(nums)+1)))

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Add each number to res and build on top of existing res for the 
        following numbers
        Time Complexity: O(n * 2^n)
        Space Complexity: O(n * 2^n)
        """
        res = [[]]
        for num in nums:
            res += [r + [num] for r in res]
        return res

    def subsets_bt(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all subsets by backtracking to generate all combinations for 
        all lengths, i.e., [C(n,0), C(n,1), C(n,2), ..., C(n,n)]
        Time Complexity: O(n * 2^n)
        Space Complexity: O(n)
        """

        def backtrack(track: List[int], start: int, k: int) -> None:
            if len(track) == k:
                res.append(track[:])
                return
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(track, i + 1, k)
                track.pop()

        res = []
        for k in range(len(nums) + 1):
            backtrack([], 0, k)
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.subsets_py(nums)
            ret2 = sol.subsets(nums)
            ret3 = sol.subsets_bt(nums)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(f"Solved using itertools:    {out}")
            print(f"Solved using backtracking: {out2}")
            print(f"Solved using backtracking: {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
