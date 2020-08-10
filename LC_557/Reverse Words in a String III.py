"""
Given a string, you need to reverse the order of characters in each word within
a sentence while still preserving whitespace and initial word order.
"""
from common_funcs import stringToString


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())
    
    def reverseWords_2(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.reverseWords(s)
            ret2 = sol.reverseWords_2(s)
            
            print(ret)
            print(ret2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
