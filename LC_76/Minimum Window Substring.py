"""
Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window. If there is no such substring, return the empty string.

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        # Unique chars and their frequencies for t and for current window
        t_count, window_count = Counter(t), Counter()
        # left and right pointer for the window
        l, r = 0, 0
        # num unique chars in t that are in current window and are required
        formed, required = 0, len(t_count)
        # window length, left, right
        ans = float('inf'), None, None

        while r < len(s):
            if s[r] in t_count:
                window_count[s[r]] += 1  # add char on the right to window
                if window_count[s[r]] == t_count[s[r]]:
                    # if char's freq reaches freq of it in t, increment formed
                    formed += 1

            # squeeze window to find min window
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:  # save min window so far
                    ans = r - l + 1, l, r

                # remove char on the left from window
                if s[l] in t_count:
                    window_count[s[l]] -= 1
                    if window_count[s[l]] < t_count[s[l]]:
                        formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]

    def minWindow_2(self, s: str, t: str) -> str:
        from collections import Counter

        # positive - we still need it; negative - we have an excess of it
        needed = Counter(t)  # how many times we need each char in t
        missing = len(t)  # how many chars still missing
        l = min_l = min_r = 0  # left/right pointers for current and min window

        for r, char in enumerate(s, 1):
            missing -= needed[char] > 0  # match a needed char
            needed[char] -= 1  # decrement freq for char

            if not missing:  # if nothing missing, squeeze window
                while l < r and needed[s[l]] < 0:
                    needed[s[l]] += 1
                    l += 1  # squeeze window for smaller window

                if not min_r or r - l < min_r - min_l:
                    min_l, min_r = l, r  # update left/right for min window

        return s[min_l: min_r]


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
