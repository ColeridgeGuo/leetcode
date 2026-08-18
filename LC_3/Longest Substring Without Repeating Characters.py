"""
Given a string, find the length of the longest substring without repeating
characters.
"""
from common_funcs import stringToList


class Solution:
    def lengthOfLongestSubstring_set(self, s: str) -> int:
        """
        Maintain a set-backed sliding window of unique characters, shrinking
        from the left whenever the next character is already in the window.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        longest = start = 0
        for end, char in enumerate(s):
            while char in seen:
                seen.remove(s[start])
                start += 1
            seen.add(char)
            longest = max(longest, len(seen)) # or (end - start + 1)
        return longest
    
    def lengthOfLongestSubstring_dict(self, s: str) -> int:
        """
        Track each character's last index and jump the window's left boundary
        past a duplicate without moving the boundary backward.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        last_seen = {}
        longest = start = 0
        for end, char in enumerate(s):
            if char in last_seen:
                start = max(start, last_seen[char] + 1)
            last_seen[char] = end
            longest = max(longest, end - start + 1)
        return longest


def main():
    while True:
        try:
            line = input()
            s = stringToList(line)
            
            sol = Solution()
            ret_s = sol.lengthOfLongestSubstring_set(s)
            ret_d = sol.lengthOfLongestSubstring_dict(s)
            
            print(f"Solved using a set:        {ret_s}")
            print(f"solved using a dictionary: {ret_d}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
