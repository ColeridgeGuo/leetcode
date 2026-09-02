"""
Given a set of candidate numbers (candidates) (without duplicates) and a target
number (target), find all unique combinations in candidates where the candidate
numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def combinationSum(self, candidates: List[int],
                         target: int) -> List[List[int]]:
        
        def backtrack(choices: List[int], remaining: int,
                      track: List[int], start: int) -> None:
            if remaining < 0:
                return
            if remaining == 0:
                res.append(track.copy())
            else:
                for i in range(start, len(choices)):
                    track.append(choices[i])  # choose
                    backtrack(choices, remaining - choices[i], track, i)
                    track.pop(-1)  # un-choose
        res = []
        backtrack(candidates, target, [], 0)
        return res

    def combinationSum_2(self, candidates: list[int],
                         target: int) -> list[list[int]]:

        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return

            for index in range(start, len(candidates)):
                candidate = candidates[index]

                if candidate > remaining:
                    break

                path.append(candidate)
                backtrack(index, remaining - candidate)
                path.pop()

        backtrack(0, target)
        return result


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret = sol.combinationSum(nums, target)
            ret2 = sol.combinationSum_2(nums, target)
            
            out = listToString(ret)
            out2 = listToString(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
