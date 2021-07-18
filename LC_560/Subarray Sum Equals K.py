"""
Given an array of integers nums and an integer k, return the total number of 
continuous subarrays whose sum equals to k.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def subarraySum_bf(self, nums: List[int], k: int) -> int:
        """
        Brute force solution: find every subarray sum
        Time Complexity: O(n^3)
        Space Complexity: O(1)
        """
        count = 0
        for start in range(len(nums)):
            for end in range(start+1, len(nums)+1):
                sum_ = 0
                for i in range(start, end):
                    sum_ += nums[i]
                if sum_ == k:
                    count += 1
        return count

    def subarraySum_cs(self, nums: List[int], k: int) -> int:
        """
        Build a cumulative sum array
        Subarray sum for [i,j] is cum_sum[j] - cum_sum[i]
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        from itertools import accumulate
        count = 0
        cum_sum = [0] + list(accumulate(nums))
        for start in range(len(nums)):
            for end in range(start+1, len(nums)+1):
                if cum_sum[end] - cum_sum[start] == k:
                    count += 1
        return count

    def subarraySum_cs2(self, nums: List[int], k: int) -> int:
        """
        Calculate cumulative sum on the go and increment count if == k
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        for start in range(len(nums)):
            sum_ = 0
            for end in range(start, len(nums)):
                sum_ += nums[end]
                if sum_ == k:
                    count += 1
        return count

    def subarraySum_hm(self, nums: List[int], k: int) -> int:
        """
        Use hashmap to store frequencies of unique cumulative sums appeared 
        and increment count if any equals k. If sum[j] - k = sum[i], then 
        subarray sum for (i, j] = k, so if sum[j] - k appears in the hashmap, we 
        know that we have seen i and that subarray sum for (i,j] = k 
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count, sum_ = 0, 0
        # dic = {0: 1}
        dic = {}
        for n in nums:
            sum_ += n
            # if cumulative sum explicitly equals to k, increment count by 1
            # these two lines can be replaced by dic = {0:1}
            if sum_ == k:
                count += 1
            count += dic.get(sum_ - k, 0)
            dic[sum_] = dic.get(sum_, 0) + 1
        return count


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.subarraySum_bf(nums, k)
            ret2 = sol.subarraySum_cs(nums, k)
            ret3 = sol.subarraySum_cs2(nums, k)
            ret4 = sol.subarraySum_hm(nums, k)

            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            out4 = str(ret4)
            print(f"Solved with brute force:              {out}")
            print(f"Solved with cumulative sum:           {out2}")
            print(f"Solved with cumulative sum on the go: {out3}")
            print(f"Solved using hashmap:                 {out4}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
