"""
Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""
from common_funcs import stringToString


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        # initialize max vowel count (ans) and current vowel count
        ans = vowel_cnt = sum(c in vowels for c in s[:k])
        for i in range(len(s) - k):  # slide the window ot the right
            # new window adds a vowel and removes a non-vowel, update ans
            if s[i] not in vowels and s[i + k] in vowels:
                vowel_cnt += 1
                ans = max(ans, vowel_cnt)
            # new window removes a vowel and adds a non-vowel, decrement count
            elif s[i] in vowels and s[i + k] not in vowels:
                vowel_cnt -= 1
            # the vowel count remains the same in all other cases
        return ans


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.maxVowels(s, k)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
