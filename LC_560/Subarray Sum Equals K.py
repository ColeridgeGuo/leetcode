"""
Given an array of integers nums and an integer k, return the total number of 
continuous subarrays whose sum equals to k.
"""
from typing import List
from common_funcs import stringToList


class Solution:

    def subarraySum_hm(self, nums: List[int], k: int) -> int:
        """
        Use hashmap to store frequencies of unique cumulative sums appeared 
        and increment count if any equals k. If sum[j] - k = sum[i], then 
        subarray sum for (i, j] = k, so if sum[j] - k appears in the hashmap, we 
        know that we have seen i and that subarray sum for (i,j] = k 
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        count, prefix_sum = 0, 0
        prefix_count = {0: 1}
        for n in nums:
            prefix_sum += n
            count += prefix_count.get(prefix_sum - k, 0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        return count


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.subarraySum_hm(nums, k)

            out = str(ret)
            print(f"Solved using hashmap: {out}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
