"""
    Write a function that reverses a string. The input string is given as an
    array of characters char[].
    
    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def reverseString_slicing(self, s: List[str]) -> None:
        s[:] = s[::-1]
        
    def reverseString_two_pointers(self, s: List[str]) -> None:
        """
            Time Complexity: O(n/2) = O(n)
            Space Complexity: O(1)
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
            
    def reverseString_recursive(self, s: List[str]) -> None:
        """
            Time Complexity: O(n/2) = O(n)
            Space Complexity: O(n)
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


def main():
    while True:
        try:
            line = input()
            import ast
            char_list_1 = ast.literal_eval(line)
            char_list_2 = ast.literal_eval(line)
            char_list_3 = ast.literal_eval(line)
            
            sol = Solution()
            sol.reverseString_slicing(char_list_1)
            sol.reverseString_two_pointers(char_list_2)
            sol.reverseString_recursive(char_list_3)

            print(f"Solved using Python list slicing: {char_list_1}")
            print(f"Solved using two pointers:        {char_list_2}")
            print(f"Solved recursively:               {char_list_3}")
            
        except StopIteration:
            break


if __name__ == '__main__':
    main()
