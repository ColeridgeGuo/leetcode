"""
You are given two 0-indexed strings s and target.

You can take some letters from s and rearrange them to form new strings.
Return the maximum number of copies of target that can be formed by taking
letters from s and rearranging them.
"""
from common_funcs import stringToString


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        s_count, target_count = Counter(s), Counter(target)
        return min(s_count[char] // target_count[char] for char in target_count)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            target = stringToString(line)

            sol = Solution()
            ret = sol.rearrangeCharacters(s, target)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
