"""
Given an arbitrary ransom note string and another string containing letters from
all the magazines, write a function that will return true if the ransom note can
be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""
from common_funcs import stringToString


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Substraction between Counters keeps only positive counts, so if some 
        chars in note are not matched in magazine, their difference would not be 
        empty so return False; otherwise all chars in note are matched so True
        """
        from collections import Counter
        return not Counter(ransomNote) - Counter(magazine)

    def canConstruct_dictionary(self, ransomNote: str, magazine: str) -> bool:
        """
        Construct a Counter using chars in magazine and match each char in note 
        to one in magazine, return False if one char in note fails to match
        """
        from collections import defaultdict
        counter = defaultdict(int)
        for char in magazine:
            counter[char] += 1
        for char in ransomNote:
            if char not in counter:
                return False
            elif counter[char] <= 0:
                return False
            else:
                counter[char] -= 1
        return True

    def canConstruct_dictionary_2(self, ransomNote: str, magazine: str) -> bool:
        """
        Same as the above method but more concise
        """
        counter = {}
        for char in magazine:
            counter[char] = counter.get(char, 0) + 1
        for char in ransomNote:
            if counter.get(char, 0) <= 0:
                return False
            counter[char] -= 1
        return True


def main():
    while True:
        try:
            line = input()
            ransomNote = stringToString(line)
            line = input()
            magazine = stringToString(line)

            sol = Solution()
            ret_cnt = sol.canConstruct(ransomNote, magazine)
            ret_dic = sol.canConstruct_dictionary(ransomNote, magazine)

            print(f"Solved using Python's Counter: {ret_cnt}")
            print(f"Solved using dictionary:       {ret_dic}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
