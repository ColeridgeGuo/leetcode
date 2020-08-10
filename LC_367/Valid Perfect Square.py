"""
    Given a positive integer num, write a function which returns True if num is
    a perfect square else False.
    
    Follow up: Do not use any built-in library function such as sqrt.
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
            Binary Search
            Time Complexity: O(lg n)
            Space Complexity: O(1)
        """
        left, right = 0, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


def main():
    while True:
        try:
            line = input()
            num = int(line)

            sol = Solution()
            ret = sol.isPerfectSquare(num)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
