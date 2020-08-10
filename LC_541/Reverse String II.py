"""
Given a string and an integer k, you need to reverse the first k characters for
every 2k characters counting from the start of the string. If there are less
than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and
left the other as original.
"""
from common_funcs import stringToString


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        temp = []
        i = 0
        for char in s:
            if i % (2 * k) < k - 1:
                temp.append(char)
            elif i % (2 * k) == k - 1:
                temp.append(char)
                res += reversed(temp)
                temp = []
            elif i % (2 * k) < 2 * k:
                res.append(char)
            i += 1
        res += reversed(temp)
        return ''.join(res)
    
    def reverseStr_2(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            line = input()
            k = int(line)

            sol = Solution()
            ret = sol.reverseStr(s, k)
            ret2 = sol.reverseStr_2(s, k)
            
            print(ret)
            print(ret2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
