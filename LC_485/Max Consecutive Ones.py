"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
            Set max_consec on encountering 0
        """
        max_consec = 0
        start, end = -1, 0
        while end < len(nums):
            if nums[end] == 0:
                max_consec = max(max_consec, end - start - 1)
                start = end
            end += 1
        return max(max_consec, end - start - 1)
    
    def findMaxConsecutiveOnes_2(self, nums: List[int]) -> int:
        """
            Set max_consec on encountering 1
        """
        max_consec = ans = 0
        for num in nums:
            if num == 1:
                max_consec += 1
                ans = max(ans, max_consec)
            else:
                max_consec = 0
        return ans


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.findMaxConsecutiveOnes(nums)
            ret2 = sol.findMaxConsecutiveOnes_2(nums)
            
            out = str(ret)
            out2 = str(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
