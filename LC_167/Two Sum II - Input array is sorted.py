"""
    Given an array of integers that is already sorted in ascending order, find
    two numbers such that they add up to a specific target number. The function
    twoSum should return indices of the two numbers such that they add up to the
    target, where index1 must be less than index2.
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def twoSum_dictionary(self, numbers: List[int], target: int) -> List[int]:
        """
            Store the complement of each number in a dictionary with its index
            as the value, and retrieve it when encountered the complement.
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num], i + 1]
            dic[num] = i + 1
    
    def twoSum_pointers(self, numbers: List[int], target: int) -> List[int]:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        ptr1, ptr2 = 0, len(numbers) - 1
        while ptr2 > ptr1:
            if numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1 + 1, ptr2 + 1]
            elif numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
            else:
                ptr2 -= 1


def main():
    while True:
        try:
            line = input()
            numbers = stringToList(line)
            line = input()
            target = int(line)
            
            sol = Solution()
            ret_dictionary = sol.twoSum_dictionary(numbers, target)
            ret_pointers = sol.twoSum_pointers(numbers, target)
            
            out_dictionary = listToString(ret_dictionary)
            out_pointers = listToString(ret_pointers)
            print(f"Solved using dictionary: {out_dictionary}")
            print(f"Solved using pointers:   {out_pointers}")
        except StopIteration:
            break
    

if __name__ == '__main__':
    main()
