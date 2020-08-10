"""
    Given a positive integer, return its corresponding column title as appear in
    an Excel sheet. For example:
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB
        ...
"""


class Solution:
    def convertToTitle_recursive(self, n: int) -> str:
        """
            Time Complexity:
            Space Complexity:
        """
        excel = chr((n - 1) % 26 + ord('A'))
        rest = (n - 1) // 26
        if not rest:
            return chr( (n - 1) % 26 + ord('A'))
        return self.convertToTitle_recursive(rest) + excel
    
    def convertToTitle_iterative(self, num):
        """
            Imitate the iterative approach to convert from base-10 to base-26:
            divide the quotient of the previous division by 26 until it can't be
            further divided; append the corresponding letter A-Z to the front of
            the output
            Time Complexity:
            Space Complexity:
        """
        chars = ""
        while num > 0:
            num, remainder = divmod(num, 26)
            if not remainder:  # force the range of remainder to be [1,26]
                num, remainder = num - 1, remainder + 26
            chars = chr(remainder - 1 + ord('A')) + chars
        return chars


def main():
    while True:
        try:
            line = input()
            n = int(line)
            
            sol = Solution()
            ret_recur = sol.convertToTitle_recursive(n)
            ret_iter = sol.convertToTitle_iterative(n)
            
            print(f"Solved recursively: {ret_recur}")
            print(f"Solved iteratively: {ret_iter}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
