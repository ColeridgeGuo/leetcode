"""
Given an array of integers and an integer k, you need to find the number of
unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(2n) = O(n)
        """
        if k < 0:
            return 0
        diff, res = set(), set()
        for i, num in enumerate(nums):
            if num + k in diff:
                res.add((num + k, num))
            if num - k in diff:
                res.add((num, num - k))
            diff.add(num)
        return len(res)
    
    def findPairs_2(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(2n) = O(n)
        Space Complexity: O(n)
        """
        from collections import Counter
        result = 0
        counter = Counter(nums)
        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result
    
    def findPairs_3(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n*log(n))
        Space Complexity: O(n)
        """
        sort = sorted(nums)
        left, right = 0, 1
        result = 0
        while left < len(sort) and right < len(sort):
            if left == right or sort[right] - sort[left] < k:
                right += 1  # diff < k, move right pointer
            elif sort[right] - sort[left] > k:
                left += 1  # diff > k, move left pointer
            else:  # diff = k
                left += 1
                result += 1
                while left < len(sort) and sort[left] == sort[left - 1]:
                    left += 1  # skip same number
        return result


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.findPairs(nums, k)
            ret2 = sol.findPairs_2(nums, k)
            ret3 = sol.findPairs_3(nums, k)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(f"Solved using two sets:     {out}")
            print(f"Solved using Counter:      {out2}")
            print(f"Solved using two pointers: {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
