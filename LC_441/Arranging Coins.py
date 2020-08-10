"""
    You have a total of n coins that you want to form in a staircase shape,
    where every k-th row must have exactly k coins. Given n, find the total
    number of full staircase rows that can be formed. n is a non-negative
    integer and fits within the range of a 32-bit signed integer.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
            Time Complexity: O(sqrt(2n)) = O(sqrt(n))
            Space Complexity: O(1)
        """
        coins = 1
        while n >= coins:
            n -= coins
            coins += 1
        return coins - 1
    
    def arrangeCoins_binary_search(self, n: int) -> int:
        """
            Time Complexity: O(lg n)
            Space Complexity: O(1)
        """
        l, r = 0, n
        while l <= r:
            mid = l + (r - l) // 2
            complete = mid * (mid + 1) // 2
            if complete == n:
                return mid
            elif complete > n:
                r = mid - 1
            else:
                l = mid + 1
        return r
    
    def arrangeCoins_math(self, n: int) -> int:
        """
            Time Complexity: O(1)
            Space Complexity: O(1)
        """
        return int((2 * n + 0.25) ** 0.5 - 0.5)


def main():
    while True:
        try:
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.arrangeCoins(n)
            ret_bs = sol.arrangeCoins_binary_search(n)
            ret_math = sol.arrangeCoins_math(n)
            
            print(ret)
            print(ret_bs)
            print(ret_math)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
