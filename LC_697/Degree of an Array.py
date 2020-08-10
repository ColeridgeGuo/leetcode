"""
Given a non-empty array of non-negative integers nums, the degree of this array
is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of
nums, that has the same degree as nums.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import defaultdict
        index = defaultdict(list)
        degree, max_nums = 0, []
        
        for i, num in enumerate(nums):
            index[num].append(i)
            if len(index[num]) > degree:
                degree = len(index[num])
                max_nums = [num]
            elif len(index[num]) == degree:
                max_nums.append(num)
        min_len = len(nums)
        for num in max_nums:
            min_len = min(min_len, index[num][-1] - index[num][0] + 1)
        return min_len
    
    def findShortestSubArray_2(self, nums: List[int]) -> int:
        first, last, count = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        min_len = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                min_len = min(min_len, last[num] - first[num] + 1)
        return min_len


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            
            sol = Solution()
            ret = sol.findShortestSubArray(nums)
            ret_2 = sol.findShortestSubArray_2(nums)
            
            print(f"Solved by storing indices of all numbers  :      {ret}")
            print(f"Solved by storing only the first and last index: {ret_2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
