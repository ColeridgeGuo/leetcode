"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        from math import ceil
        res = []
        n = len(s)
        cycle = num_rows + (num_rows - 2)
        for offset in range(num_rows):
            for i in range(ceil(n / cycle) + 1):
                idx = i * cycle
                if offset in {0, num_rows - 1}:
                    if idx + offset < n:
                        res.append(s[idx + offset])
                else:
                    if 0 <= idx - offset < n:
                        res.append(s[idx - offset])
                    if idx + offset < n:
                        res.append(s[idx + offset])
        return ''.join(res)

    def convert_2(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        res = []
        n = len(s)
        cycle = num_rows + (num_rows - 2)
        for offset in range(num_rows):
            for i in range(0, n - offset, cycle):
                res.append(s[i + offset])
                if (offset != 0 and offset != num_rows - 1
                        and i + cycle - offset < n):
                    res.append(s[i + cycle - offset])
        return ''.join(res)

    def convert_3(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s
        ans = [''] * num_rows
        index, step = 0, 1
        for x in s:
            ans[index] += x
            if index == 0:
                step = 1
            elif index == num_rows - 1:
                step = -1
            index += step
        return ''.join(ans)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            num_rows = int(line)

            sol = Solution()
            ret = sol.convert(s, num_rows)
            ret2 = sol.convert_2(s, num_rows)
            ret3 = sol.convert_3(s, num_rows)

            out = stringToString_out(ret)
            out2 = stringToString_out(ret2)
            out3 = stringToString_out(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
