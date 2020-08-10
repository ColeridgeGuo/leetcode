"""
Write a function that takes a string as input and reverse only the vowels of a
string.
"""
from common_funcs import stringToString


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            if chars[l] not in vowels:
                l += 1
            if chars[r] not in vowels:
                r -= 1
        return ''.join(chars)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            ret = Solution().reverseVowels(s)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()