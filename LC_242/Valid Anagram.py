"""
Given two strings s and t , write a function to determine if t is an anagram of
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
            Time Complexity: O(2*n) = O(n)
            Space Complexity: O(2*n) = O(n)
        """
        from collections import defaultdict
        dic_s, dic_t = defaultdict(int), defaultdict(int)
        for char in s:
            dic_s[char] += 1
        for char in t:
            dic_t[char] += 1
        return dic_s == dic_t
    
    def isAnagram_dictionary_2(self, s: str, t: str) -> bool:
        """
            Time Complexity: O(3*n) = O(n)
            Space Complexity: O(n)
        """
        from collections import defaultdict
        alphabet = defaultdict(int)
        for char in s:
            alphabet[char] += 1
        for char in t:
            alphabet[char] -= 1
        for val in alphabet.values():
            if val != 0:
                return False
        return True
    
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
            ret_dic2 = sol.isAnagram_dictionary_2(s, t)
            ret_sort = sol.isAnagram_sort(s, t)
            print(f"Solved using Counter:          {ret_counter}")
            print(f"Solved using two dictionaries: {ret_dic}")
            print(f"Solved using one dictionary:   {ret_dic2}")
            print(f"Solved using sorted:           {ret_sort}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
