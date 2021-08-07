"""
Given a string s, return the last substring of s in lexicographical order.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def lastSubstring_slow(self, s: str) -> str:
        """
        Generate all substrings of s and sort them alphabetically (TLE)
        Time Complexity: O(n^2) for all substrings and O(n*log(n)) for sorting
        Space Complexity: O(n^2)
        """
        from itertools import combinations
        return sorted(s[x:y] for x, y in combinations(range(len(s)+1), r=2))[-1]

    def lastSubstring(self, s: str) -> str:
        """
        Start by finding all the positions of the largest letters in s, the 
        valid last substring must start with of them. Then compare their next 
        letters and ignore substring with alphabetically smaller letters. 
        Repeat this process until only one substring is left. 
        We filter out the ones near the end, and the ones that start with the 
        largest letter following another largest char.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        import collections
        import re

        largest_char = max(s)  # largest letter in s
        # all indices of largest char
        count = [match.start() for match in re.finditer(largest_char, s)]
        # indices of largest substrings and their next chars to compare
        largest_pos = {pos: pos + 1 for pos in count}

        while len(largest_pos) > 1:
            filtered = set()  # the ones to be filtered out
            # chars following current largest char and the starting indices of
            # the substring from which they are in
            next_char = collections.defaultdict(list)
            for start in largest_pos:
                # filter out if reaching the end
                if largest_pos[start] == len(s):
                    filtered.add(start)
                # keep track of next char's pos for later comparing
                else:
                    next_char[s[largest_pos[start]]].append(start)
                # filter out the latter largest char if two are adjacent
                if largest_pos[start] in largest_pos:
                    filtered.add(largest_pos[start])

            # find the new largest char, filter out the alphabetically smaller
            # substrings, and update the next chars to compare
            next_starts = {
                start: largest_pos[start]+1
                for start in next_char[max(next_char)] if start not in filtered}
            largest_pos = next_starts  # repeat with new chars

        for start in largest_pos:
            return s[start:]

    def lastSubstring_2(self, s: str) -> str:
        """
        Pointer i is the starting index of the result substring; pointer j is 
        the look ahead w/ which to compare i. When s[i] and s[j] are the same, 
        compare the chars next to them by using offset k; otherwise reset k. If 
        s[j] is alphabetically greater than s[i], meaning s[i:] is no longer the 
        last substring, set i to j (or i+k+1 to skip duplicates); otherwise if 
        s[j] is smaller, just move j k+1 steps ahead to keep comparing.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i, j, offset = 0, 1, 0
        while j + offset < len(s):
            if s[j+offset] == s[i+offset]:
                # increment offset if next chars are still the same
                offset += 1
            elif s[j+offset] < s[i+offset]:
                j += offset + 1  # skip the next k+1 chars
                offset = 0       # reset k
            else:
                # new alphabetically larger char found
                i = max(i + offset + 1, j)
                j = i + 1   # start j from i's next
                offset = 0  # reset k
        return s[i:]


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.lastSubstring(s)
            ret2 = sol.lastSubstring_2(s)
            ret3 = sol.lastSubstring_slow(s)

            out = stringToString_out(ret)
            out2 = stringToString_out(ret2)
            out3 = stringToString_out(ret3)
            print(f"Solved by filtering out substrings w/ sets:     {out}")
            print(f"Solved by filtering out substrings w/ pointers: {out2}")
            print(f"Solved by generating all substrings:            {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
