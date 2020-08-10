"""

"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        from math import ceil
        res = []
        n = len(s)
        cycle = numRows + (numRows - 2)
        for offset in range(numRows):
            for i in range(ceil(n / cycle) + 1):
                idx = i * cycle
                if offset in {0, numRows - 1}:
                    if idx + offset < n:
                        res.append(s[idx + offset])
                else:
                    if 0 <= idx - offset < n:
                        res.append(s[idx - offset])
                    if idx + offset < n:
                        res.append(s[idx + offset])
        return ''.join(res)
    
    def convert_2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        n = len(s)
        cycle = numRows + (numRows - 2)
        for offset in range(numRows):
            for i in range(0, n - offset, cycle):
                res.append(s[i + offset])
                if offset != 0 and offset != numRows - 1 and i + cycle - offset < n:
                    res.append(s[i + cycle - offset])
        return ''.join(res)
    
    def convert_3(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        return ''.join(L)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            numRows = int(line)
            
            sol = Solution()
            ret = sol.convert(s, numRows)
            ret2 = sol.convert_2(s, numRows)
            ret3 = sol.convert_3(s, numRows)
            
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
