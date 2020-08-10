"""
Given scores of N athletes, find their relative ranks and the people with the
top three highest scores, who will be awarded medals: "Gold Medal", "Silver
Medal" and "Bronze Medal".
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        ranks = {num: i + 1 for i, num in enumerate(sorted(nums, reverse=True))}
        rank_names = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        return [rank_names.get(ranks[num], str(ranks[num])) for num in nums]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.findRelativeRanks(nums)
            
            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
