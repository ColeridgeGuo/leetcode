"""
    You are a product manager and currently leading a team to develop a new
    product. Unfortunately, the latest version of your product fails the quality
    check. Since each version is developed based on the previous version, all
    the versions after a bad version are also bad.
    
    Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad.
    
    You are given an API bool isBadVersion(version) which will return whether
    version is bad. Implement a function to find the first bad version. You
    should minimize the number of calls to the API.
"""


BAD_VERSION = 0


def isBadVersion(version: int) -> int:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
            Time Complexity: O(lg n)
            Space Complexity: O(1)
        """
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high


def main():
    while True:
        try:
            line = input()
            n = int(line)
            line = input()
            bad = int(line)
            global BAD_VERSION
            BAD_VERSION = bad
            
            sol = Solution()
            ret = sol.firstBadVersion(n)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
