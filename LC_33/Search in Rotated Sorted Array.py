"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if you found return its index,
otherwise return -1.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def search_side_inf(self, nums: List[int], target: int) -> int:
        """
        treat the half that does not include target as all +/-∞'s, e.g.,
        if target = 5, [4,5,6,7,1,2,3] becomes [4,5,6,7,∞,∞,∞];
        if target = 2, [4,5,6,7,1,2,3] becomes [-∞,-∞,-∞,-∞,1,2,3].
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                num = nums[mid]
            else:
                num = float('-inf') if target < nums[0] else float('inf')
            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid - 1
            else:
                return mid
        return -1
    
    def search_side(self, nums: List[int], target: int) -> int:
        """
        Similar to the above method without explicitly using +/-inf. When target
        and nums[mid] are on the same side, perform regular binary search;
        otherwise ditch the part to which target doesn't belong
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid
            elif target < nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
    
    def search_rotate(self, nums: List[int], target: int) -> int:
        """
        0 1 2 3 4 5 6 7
        4 5 6 7 0 1 2 3     (original + rot) % N = rotated num
        rotation length = 4
        """
        lo, hi = 0, len(nums) - 1
        # find the smallest num to know the rotation length
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        rot = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            real_mid = (mid + rot) % len(nums)  # find real pos w/ rotation len
            if nums[real_mid] < target:
                lo = mid + 1
            elif nums[real_mid] > target:
                hi = mid - 1
            else:
                return real_mid
        return -1
    
    def search_ordered_side(self, nums: List[int], target: int) -> int:
        """
        Any split to nums splits into two parts: one in order and one not
        inorder, e.g., [4,5,6,7,1,2,3] => [4,5,6] & [7,1,2,3], then if target is
        in the ordered part, we ditch the unordered part; otherwise we ditch
        this part
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            if nums[lo] <= nums[mid]:  # left side is ordered
                if nums[lo] <= target <= nums[mid]:  # target in this part
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right side is ordered
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret_s1 = sol.search_side(nums, target)
            ret_s2 = sol.search_side_inf(nums, target)
            ret_r = sol.search_rotate(nums, target)
            ret_o = sol.search_ordered_side(nums, target)
            
            out_s1 = str(ret_s1)
            out_s2 = str(ret_s2)
            out_r = str(ret_r)
            out_o = str(ret_o)
            print(f"Solved by finding the side where target belongs: {out_s1}")
            print(f"Solved by treating the other side as +/-inf:     {out_s2}")
            print(f"Solved by finding the rotating length:           {out_r}")
            print(f"Solved by finding the ordered side:              {out_o}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
