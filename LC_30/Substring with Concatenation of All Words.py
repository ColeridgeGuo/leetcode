"""
You are given a string, s, and a list of words, words, that are all of the same
length. Find all starting indices of substring(s) in s that is a concatenation
of each word in words exactly once and without any intervening characters.
"""
from typing import List
from common_funcs import stringToList, stringToString, listToString


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        from collections import Counter
        counts, res = Counter(words), []
        word_len, num_words = len(words[0]), len(words)
        total_len = word_len * num_words
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(i, i + total_len, word_len):
                curr_word = s[j:j + word_len]
                if curr_word in counts:
                    seen[curr_word] = seen.get(curr_word, 0) + 1
                    if seen[curr_word] > counts[curr_word]:
                        break
                else:
                    break
            if seen == counts:
                res.append(i)
        return res


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            words = stringToList(line)
            
            sol = Solution()
            ret = sol.findSubstring(s, words)
            
            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
