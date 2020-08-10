"""
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard
"""
from typing import List
from common_funcs import stringToList, listToString


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [set('QWERTYUIOP'), set('ASDFGHJKL'), set('ZXCVBNM')]
        return [word for word in words
                for row in keyboard if set(word.upper()).issubset(row)]

    def findWords_re(self, words: List[str]) -> List[str]:
        import re
        pattern = re.compile(r'^([qwertyuiop]+|[asdfghjkl]+|[zxcvbnm]+)$', re.I)
        return [word for word in words if re.match(pattern, word)]


def main():
    while True:
        try:
            line = input()
            words = stringToList(line)
            
            sol = Solution()
            ret = sol.findWords(words)
            ret_re = sol.findWords_re(words)
            
            out = listToString(ret)
            out_re = listToString(ret_re)
            print(f"Solved using set: {out}")
            print(f"Solved using re:  {out_re}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
