"""
Anti-theft security devices are activated inside a bank. You are given a
0-indexed binary string array bank representing the floor plan of the bank,
which is an m x n 2D matrix. bank[i] represents the ith row, consisting of
'0's and '1's. '0' means the cell is empty, while'1' means the cell has a
security device.

There is one laser beam between any two security devices if both conditions are
met:
1. The two devices are located on two different rows: r1 and r2, where r1 < r2.
2. For each row_i where r1 < i < r2, there are no security devices in the i-th
row.

Return the total number of laser beams in the bank.
"""
from typing import List
from common_funcs import stringToList


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for row in bank:
            curr = row.count('1')
            # if current row has devices, then num of laser beams between
            # previous row and current row is prev * curr
            if curr:
                ans += prev * curr
                prev = curr
        return ans


def main():
    while True:
        try:
            line = input()
            bank = stringToList(line)

            sol = Solution()
            ret = sol.numberOfBeams(bank)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
