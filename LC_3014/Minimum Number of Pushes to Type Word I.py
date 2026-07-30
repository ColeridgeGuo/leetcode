"""
You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase
English letters, which can be used to form words by pushing them.
For example, the key 2 is mapped with ["a","b","c"], we need to push the key
one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of
letters. The keys can be remapped to any amount of letters, but each letter
must be mapped to exactly one key. You need to find the minimum number of
times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping.
"""
from common_funcs import stringToString


class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Divide the letters into groups of eight, where each group uses the same
        number of pushes. The full groups cost 8 times the sum of their push
        counts, and the remainder uses one additional push per letter.
        for example: abcdefghijklmnopqrstuvwxyz - 26 letters
        1 push: a b c d e f g h
        2 push: i j k l m n o p
        3 push: q r s t u v w x
        4 push: y z
        Total pushes: 8 * (1 + 2 + 3) + 2 * 4 = 56
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        q, r = divmod(len(word), 8)
        return (1 + q) * q // 2 * 8 + r * (q + 1)


def main():
    while True:
        try:
            line = input()
            word = stringToString(line)

            sol = Solution()
            ret = sol.minimumPushes(word)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
