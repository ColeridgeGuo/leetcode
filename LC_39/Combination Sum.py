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
        
        def backtrack(choices: List[int], target: int,
                      track: List[int], answer: List[List[int]]) -> None:
            if target < 0:
                return
            if target == 0:
                answer.append(track)
                return
            for i in range(len(choices)):
                backtrack(choices[i:], target-choices[i],
                          track+[choices[i]], answer)
                
        res = []
        backtrack(candidates, target, [], res)
        return res
    
    def combinationSum_2(self, candidates: List[int],
                         target: int) -> List[List[int]]:
        
        def backtrack(choices: List[int], target: int,
                      track: List[int], start: int) -> None:
            if target < 0:
                return
            elif target == 0:
                # need to create a copy of track; unlike the previous method
                # where 'track + [choices[i]]' creates a new list
                res.append(track[:])
            else:
                for i in range(start, len(choices)):
                    track.append(choices[i])  # choose
                    backtrack(choices, target - choices[i], track, i)
                    track.pop(-1)  # un-choose
        res = []
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
