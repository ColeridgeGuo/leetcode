"""
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def permute_itertools(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(perm) for perm in permutations(nums)]

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(res: List[List[int]], nums: List[int], track: List[int]):
            if len(track) == len(nums):
                res.append(track[:])
            else:
                for n in nums:
                    if n in track:
                        continue
                    # choose
                    track.append(n)
                    # backtrack
                    backtrack(res, nums, track)
                    # unchoose
                    track.pop()

        backtrack(res, nums, [])
        return res


def main():
    while True:
        try:
            line = input()
            nums1 = stringToList(line)
            nums2 = stringToList(line)

            sol = Solution()
            ret = sol.permute_itertools(nums1)
            ret2 = sol.permute(nums2)

            out = listToString(ret)
            out2 = listToString(ret2)
            print(f"Solved using itertools's permutations: {out}")
            print(f"Solved using backtrack:                {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
