"""
Given a string, find the length of the longest substring without repeating
characters.
"""
from common_funcs import stringToList


class Solution:
    def lengthOfLongestSubstring_hashset(self, s: str) -> int:
        hashset = set()
        ans = start = end = 0
        while start < len(s) and end < len(s):
            if s[end] not in hashset:
                hashset.add(s[end])
                end += 1
                ans = max(ans, end - start)
            else:
                hashset.remove(s[start])
                start += 1
        return ans
    
    def lengthOfLongestSubstring_dict(self, s: str) -> int:
        dic = {}
        ans = start = 0
        for i, char in enumerate(s):
            if char in dic and start <= dic[char]:
                start = dic[char] + 1
            ans = max(ans, i - start + 1)
            dic[char] = i
        return ans


def main():
    while True:
        try:
            line = input()
            s = stringToList(line)
            
            sol = Solution()
            ret_s = sol.lengthOfLongestSubstring_hashset(s)
            ret_d = sol.lengthOfLongestSubstring_dict(s)
            
            print(f"Solved using hashset:    {ret_s}")
            print(f"solved using dictionary: {ret_d}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
