"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.
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

    def reverseVowels_2(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        ans = []
        s_vowels = []
        for i in range(len(s)):
            if s[i] in vowels:
                s_vowels.append(s[i])
                ans.append("")
            else:
                ans.append(s[i])
        j = -1
        for i in range(len(ans)):
            if ans[i] == "":
                ans[i] = s_vowels[j]
                j -= 1
        return ''.join(ans)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()

            ret = sol.reverseVowels(s)
            ret2 = sol.reverseVowels_2(s)
            
            print(f"Solved by moving pointers:         {ret}")
            print(f"Solved by constructing new string: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()