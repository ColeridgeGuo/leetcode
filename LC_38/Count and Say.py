"""
The count-and-say sequence is a sequence of digit strings defined by the 
recursive formula:
    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from 
        countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of 
groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. To 
convert the saying into a digit string, replace the counts with a number and 
concatenate every saying.
Given a positive integer n, return the nth term of the count-and-say sequence.
"""


class Solution:
    def countAndSay_recur(self, n: int) -> str:
        # Base case
        if n <= 1:
            return '1'
        # Recursive case
        return self.compress(self.countAndSay_recur(n-1))

    def compress(self, s: str) -> str:
        L = []
        prev = ''
        count = 1
        for char in s:
            if char != prev:
                if prev:
                    L.append((count, prev))
                count = 1
                prev = char
            else:
                count += 1
        L.append((count, s[-1]))
        return ''.join(f'{a}{b}' for a, b in L)

    def countAndSay_iter(self, n: int) -> int:
        s = ['1']
        for _ in range(n-1):
            prev, temp, count = s[0], [], 0
            for char in s:
                if char != prev:
                    temp += [f'{count}', prev]
                    count = 1
                    prev = char
                else:
                    count += 1
            temp += [f'{count}', prev]
            s = temp
        return ''.join(s)


def main():
    while True:
        try:
            line = input()
            n = int(line)

            sol = Solution()
            ret = sol.countAndSay_recur(n)
            ret2 = sol.countAndSay_iter(n)

            print(f"Solved recursively: {ret}")
            print(f"Solved iteratively: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
