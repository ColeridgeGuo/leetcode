"""
Given a word, you need to judge whether the capitals are used right or not.
We define the usage of capitals in a word to be right when one of the following
cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Otherwise, we define that this word doesn't use capitals in a right way.
"""
from common_funcs import stringToString


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
    
    def detectCapitalUse_2(self, word: str) -> bool:
        return word[1:] == word[1:].lower() or word == word.upper()

    def detectCapitalUse_re(self, word: str) -> bool:
        import re
        return bool(re.fullmatch(r'[A-Z]*|.[a-z]*', word))

    def detectCapitalUse_3(self, word: str) -> bool:
        c = 0
        for i in word:
            if i == i.upper():
                c += 1
        return c == len(word) or (c == 1 and word[0] == word[0].upper()) or not c


def main():
    while True:
        try:
            line = input()
            word = stringToString(line)

            sol = Solution()
            ret = sol.detectCapitalUse(word)
            ret2 = sol.detectCapitalUse_2(word)
            ret_re = sol.detectCapitalUse_re(word)
            ret3 = sol.detectCapitalUse_3(word)
            
            print(ret)
            print(ret2)
            print(ret_re)
            print(ret3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
