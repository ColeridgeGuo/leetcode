"""
    Given an array of integers and an integer k, find out whether there are two
    distinct indices i and j in the array such that nums[i] = nums[j] and the
    absolute difference between i and j is at most k.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if abs(dic.get(num, k+i+1) - i) <= k:
                return True
            dic[num] = i
        return False


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)
            
            sol = Solution()
            ret = sol.containsNearbyDuplicate(nums, k)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()