"""
Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window. If there is no such substring, return the empty string.

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""
from common_funcs import stringToString, stringToString_out
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Expand a sliding window and count distinct required characters whose
        frequencies are satisfied. Shrink each valid window to find the shortest.

        Time Complexity: O(m + n), where m = len(s), n = len(t).
        Space Complexity: O(k) auxiliary space, where k is the number of distinct
        characters in s and t combined; the returned substring uses O(m) space.
        """
        window, need = Counter(), Counter(t)
        formed, required = 0, len(need)

        best_start = best_end = 0
        left = 0

        for right, right_char in enumerate(s):
            window[right_char] += 1

            if right_char in need and window[right_char] == need[right_char]:
                formed += 1

            while formed == required:
                if not best_end or right - left + 1 < best_end - best_start:
                    best_start, best_end = left, right + 1

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1
        return s[best_start: best_end]

    def minWindow_2(self, s: str, t: str) -> str:
        """
        Track character deficits and the total missing count in a sliding window.
        Once valid, remove surplus characters from the left and record the shortest
        window, keeping it valid as the right boundary advances.

        Time Complexity: O(m + n), where m = len(s), n = len(t).
        Space Complexity: O(k) auxiliary space, where k is the number of distinct
        characters in s and t combined; the returned substring uses O(m) space.
        """
        deficit = Counter(t)  # positive means missing; negative means surplus
        missing_count = len(t)  # total missing characters, including duplicates
        left = best_start = best_end = 0  # best window is [best_start, best_end)

        for right, right_char in enumerate(s, 1):  # exclusive right boundary
            missing_count -= deficit[right_char] > 0  # match a needed char
            deficit[right_char] -= 1  # reduce the deficit for the added character

            if not missing_count:  # if nothing missing, squeeze window
                while left < right and deficit[s[left]] < 0:
                    deficit[s[left]] += 1
                    left += 1  # squeeze window for smaller window

                if not best_end or right - left < best_end - best_start:
                    best_start, best_end = left, right  # update best window boundaries

        return s[best_start: best_end]


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            t = stringToString(line)

            sol = Solution()
            ret = sol.minWindow(s, t)
            ret2 = sol.minWindow_2(s, t)

            out = stringToString_out(ret)
            out2 = stringToString_out(ret2)
            print(f"Solved using sliding window:   {out}")
            print(f"Solved using sliding window 2: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
