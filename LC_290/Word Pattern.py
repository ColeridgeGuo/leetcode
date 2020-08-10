"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.
"""
from common_funcs import stringToString


class Solution:
    def wordPattern_dictionary(self, pattern: str, str: str) -> bool:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        words = str.split()
        if len(pattern) != len(words):
            return False  # if pattern and str has different lengths
        pattern_word_map, words_matched = {}, set()
        for i, pt in enumerate(pattern):
            if pattern_word_map.get(pt, False):
                if words[i] != pattern_word_map[pt]:
                    return False  # if the patterns matches a different word
            elif words[i] in words_matched:
                return False  # if the word has been matched
            else:
                pattern_word_map[pt] = words[i]  # map pattern to word
                words_matched.add(words[i])  # mark word as matched
        return True
    
    def wordPattern_zip(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        return len(set(zip(pattern, str))) == len(set(pattern)) == len(set(str))


def main():
    while True:
        try:
            line = input()
            pattern = stringToString(line)
            line = input()
            string = stringToString(line)
            
            sol = Solution()
            ret_dic = sol.wordPattern_dictionary(pattern, string)
            ret_zip = sol.wordPattern_zip(pattern, string)
            
            print(f"Solved using dictionary and set:            {ret_dic}")
            print(f"Solved by zipping pattern and str together: {ret_zip}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
