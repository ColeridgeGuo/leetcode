class Solution:
    def addDigits_string(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(int(d) for d in str(num))
        return num

    def addDigits_digit(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
        
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
        return digital_root
    
    def addDigits_math(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


def main():
    while True:
        try:
            line = input()
            num = int(line)
            
            sol = Solution()
            ret_str = sol.addDigits_string(num)
            ret_d = sol.addDigits_digit(num)
            ret_mth = sol.addDigits_math(num)
            
            print(f"Solved by converting to string to add up digits: {ret_str}")
            print(f"Solved by adding up digits w/o converting to str:{ret_d}")
            print(f"Solved using digital root:                       {ret_mth}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
