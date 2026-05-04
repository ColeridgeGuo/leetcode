"""
Given two strings s and t, write a function to determine if t is an anagram of
s.
"""
from common_funcs import stringToString


class Solution:
    def isAnagram_counter(self, s: str, t: str) -> bool:
        """
            Time Complexity: O(2*n) = O(n)
            Space Complexity: O(2*n) = O(n)
        """
        from collections import Counter
        return Counter(s) == Counter(t)
    
    def isAnagram_dictionary(self, s: str, t: str) -> bool:
        """
            Time Complexity: O(3*n) = O(n)
            Space Complexity: O(n)
        """
        alphabet = {}
        for char in s:
            alphabet[char] = alphabet.get(char, 0) + 1
        for char in t:
            alphabet[char] = alphabet.get(char, 0) - 1
        return all(alphabet[key] == 0 for key in alphabet)
    
    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            t = stringToString(line)
            
            sol = Solution()
            ret_counter = sol.isAnagram_counter(s, t)
            ret_dic = sol.isAnagram_dictionary(s, t)
            ret_sort = sol.isAnagram_sort(s, t)
            print(f"Solved using Counter:      {ret_counter}")
            print(f"Solved using dictionaries: {ret_dic}")
            print(f"Solved using sorted:       {ret_sort}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
