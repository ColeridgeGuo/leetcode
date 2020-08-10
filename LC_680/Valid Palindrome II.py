"""
Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.
"""
from common_funcs import stringToString


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Suppose we want to know whether s[i:j] form a palindrome. If s[i] == s[j]
        then we may take i++; j--. Otherwise, the palindrome must be either
        s[i+1:j] or s[i:j-1], and we should check both cases.
        """
        
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) + ~i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True
    
    def validPalindrome_2(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                sub1, sub2 = s[left:right], s[left + 1:right + 1]
                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
            left, right = left + 1, right - 1
        return True


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret = sol.validPalindrome(s)
            ret_2 = sol.validPalindrome_2(s)
            
            print(ret)
            print(ret_2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
