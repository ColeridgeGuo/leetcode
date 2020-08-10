"""
Given two strings s and t, determine if they are isomorphic. Two strings are
isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.
"""
from common_funcs import stringToString


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        # char_map maps each char in s to a char in t
        # char_set contains all chars in t to which are mapped from s
        char_map, char_set = {}, set()
        for i, schar in enumerate(s):
            tchar = t[i]
            if schar not in char_map:  # if schar does not map to anything yet
                if tchar in char_set:  # No two chars may map to the same char
                    return False
                else:
                    char_map[schar] = tchar  # map schar to tchar
                    char_set.add(tchar)
            elif char_map[schar] != tchar:
                # not isomorphic if schar may map to a different tchar
                return False
        return True


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            t = stringToString(line)
            
            sol = Solution()
            ret = sol.isIsomorphic(s, t)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
