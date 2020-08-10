"""
    A happy number is a number defined by the following process: Starting with
    any positive integer, replace the number by the sum of the squares of its
    digits, and repeat the process until the number equals 1 (where it will
    stay), or it loops endlessly in a cycle which does not include 1. Those
    numbers for which this process ends in 1 are happy numbers.
    
    Return True if n is a happy number, and False if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
            After trials and trials, it was found that a non-happy number may be
            stuck in a loop like this: 37, 58, 89, 145, 42, 20, 4, 16, 37, ...
            There are 2 ways to get 37: 16 or 61, therefore if 16 or 61 (or 0)
            is seen during the process, it can be determined that it is not a
            happy number; otherwise it will eventually converge to 1.
            Time Complexity: O()
            Space Complexity: O(log_10(n))
        """
        while n != 1:
            if n == 16 or n == 61 or n == 0:
                return False
            n = sum(int(d) ** 2 for d in str(n))
        return True
    
    def isHappy_set(self, n: int) -> bool:
        nums_seen = {n}
        while n != 1:
            n = sum(int(d) ** 2 for d in str(n))
            if n in nums_seen:
                return False
            else:
                nums_seen.add(n)
        return True
    
    def isHappy_floyd(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow, fast = self.slow_fast_run(slow, fast)
            if fast == 1:
                return True
            if slow == fast:
                break
        return False
    
    def slow_fast_run(self, slow: int, fast: int) -> tuple:
        slow = sum(int(d) ** 2 for d in str(slow))
        fast = sum(int(d) ** 2 for d in str(fast))
        fast = sum(int(d) ** 2 for d in str(fast))
        return slow, fast

def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret = sol.isHappy(n)
            ret_set = sol.isHappy_set(n)
            ret_floyd = sol.isHappy_floyd(n)
            
            print(f"Solved numerically:                          {ret}")
            print(f"Solved with hash set:                        {ret_set}")
            print(f"Solved with Floyd Cycle Detection algorithm: {ret_floyd}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
