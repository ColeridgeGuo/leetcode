"""
Given a string s and a string t, check if s is subsequence of t.
    
A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters.c
"""
import bisect
import collections

from common_funcs import stringToString


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(|t|)
        Space Complexity:O(1)
        """
        p1 = p2 = 0
        while p1 < len(s):
            try:
                if s[p1] == t[p2]:
                    p1 += 1
                p2 += 1
            except IndexError:
                return False
        return True

    def isSubsequence_2(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(|t|)
        Space Complexity:O(1)
        """
        ps = 0
        for c in t:
            if ps < len(s) and s[ps] == c:
                ps += 1
        return ps == len(s)
    
    def isSubsequence_iter(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(|s| + |t|)
        Space Complexity: O(1)
        """
        return all(c in iter(t) for c in s)

    def isSubsequence_bisect(self, s, t):
        """
        Record the indexes for each character in t, if s[i] matches t[j], then
        s[i+1] should match a character in t with index bigger than j. This can
        be reduced to find the first element larger than a value in a sorted
        array (find upper bound), which can be achieved using binary search.

        Time Complexity: O(|t|) for setting up idx, O(lg(|s|)) for each s
        Space Complexity: O(|t|)
        """
        
        # map of all indices of each occurrence of every char in t
        pos_map = collections.defaultdict(list)
        for i, char in enumerate(t):
            pos_map[char].append(i)

        # lowBound is the minimum index the current char has to be at.
        lower_bound = 0
        for i, char in enumerate(s):
            # try to find an index that is larger than or equal to lowBound
            j = bisect.bisect_left(pos_map[char], lower_bound)
            if j == len(pos_map[char]):
                return False
            lower_bound = pos_map[char][j] + 1
        return True


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            t = stringToString(line)

            sol = Solution()
            ret_1 = sol.isSubsequence(s, t)
            ret_2 = sol.isSubsequence_2(s, t)
            ret_iter = sol.isSubsequence(s, t)
            ret_bi = sol.isSubsequence_bisect(s, t)
            
            print(f"Solved using two pointers:    {ret_1}")
            print(f"Solved using two pointers 2:  {ret_2}")
            print(f"Solved using iter():          {ret_iter}")
            print(f"Solved using binary search:   {ret_bi}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
