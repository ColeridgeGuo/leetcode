"""
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate numbers
sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        def backtrack(choices: List[int], target: int,
                      track: List[int], start: int) -> None:
            if target < 0:
                return
            elif target == 0:
                res.append(track[:])
            else:
                for i in range(start, len(choices)):
                    if i > start and choices[i] == choices[i-1]:
                        # 'i > start' means choices[start] has already been
                        # processed, and we have found all combinations starting
                        # from position 'start', hence we could skip ahead to
                        # avoid duplicate combinations
                        continue
                    track.append(choices[i])
                    backtrack(choices, target - choices[i], track, i + 1)
                    track.pop(-1)
                    # the above 3 lines are the same as this one-liner:
                    # backtrack(choices, target - choices[i],
                    #           track + [choices[i]], i + 1)
                    
        res = []
        candidates.sort()
        backtrack(candidates, target, [], 0)
        return res


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret = sol.combinationSum2(nums, target)
            
            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
