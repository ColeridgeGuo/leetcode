"""
    Given a non-empty array of integers, return the third maximum number in this
    array. If it does not exist, return the maximum number. The time complexity
    must be in O(n).
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = max(nums)
        nums = list(filter(first_max.__ne__, nums))
        if not nums:
            return first_max
        second_max = max(nums)
        nums = list(filter(second_max.__ne__, nums))
        return max(nums) if nums else first_max
    
    def thirdMax_scalable(self, nums: List[int]) -> int:
        v = (float('-inf'), float('-inf'), float('-inf'))
        for num in nums:
            if num not in v:
                if num > v[0]:
                    v = (num, v[0], v[1])
                elif num > v[1]:
                    v = (v[0], num, v[1])
                elif num > v[2]:
                    v = (v[0], v[1], num)
        return v[0] if float('-inf') in v else v[2]


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.thirdMax(nums)
            ret_sc = sol.thirdMax_scalable(nums)
            
            print(f"Solved by removing largest and second largest:   {ret}")
            print(f"Solved by keeping tracking of the three largest: {ret_sc}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
