"""
Given a collection of numbers, nums, that might contain duplicates, return all 
possible unique permutations in any order.
"""
from typing import Counter, List

from common_funcs import listToString, stringToList


class Solution:
    def permuteUnique_itertools(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(x) for x in set(permutations(nums))]
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        res = []

        def backtrack(counter: Counter, track: List[int]):
            if len(track) == len(nums):
                res.append(track[:])
                return 
            for n in set(nums):
                if counter[n] > 0:
                    # choose
                    track.append(n)
                    counter[n] -= 1
                    # backtrack
                    backtrack(counter, track)
                    # unchoose
                    track.pop()
                    counter[n] += 1
        
        backtrack(Counter(nums), [])
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.permuteUnique_itertools(nums)
            ret2 = sol.permuteUnique(nums)

            out = listToString(sorted(ret))
            out2 = listToString(sorted(ret2))
            print(f"Solved using itertools' permutations: {out}")
            print(f"Solved using backtracking:            {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
