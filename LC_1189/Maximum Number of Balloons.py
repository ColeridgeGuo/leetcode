"""
Given a string text, use its characters to form as many instances of the word
"balloon" as possible. Each character can be used at most once.

Return the maximum number of instances that can be formed.
"""
from common_funcs import stringToString


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        text_count = Counter(text)
        balloon = Counter("balloon")
        return min(text_count[char] // balloon[char] for char in balloon)

def main():
    while True:
        try:
            line = input()
            text = stringToString(line)

            sol = Solution()
            ret = sol.maxNumberOfBalloons(text)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
