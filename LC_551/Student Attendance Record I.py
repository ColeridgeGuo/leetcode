"""
You are given a string representing an attendance record for a student. The
record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than
one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his
attendance record.
"""
from common_funcs import stringToString


class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = l_count = 0
        for i, char in enumerate(s):
            if char == 'A':
                a_count += 1
            elif char == 'L':
                if i > 0 and s[i - 1] == 'L':
                    l_count += 1
                else:
                    l_count = 1
            if a_count > 1:
                return False
            if l_count > 2:
                return False
        return True
    
    def checkRecord_2(self, s: str) -> bool:
        a_count = l_count = 0
        for char in s:
            if char == 'A':
                a_count += 1
            if char == 'L':
                l_count += 1
            else:
                l_count = 0
            if a_count > 1 or l_count > 2:
                return False
        return True
    
    def checkRecord_re(self, s: str) -> bool:
        import re
        return len(re.findall(r'A', s)) < 2 and not re.findall(r'L{3,}', s)
    
    def checkRecord_re2(self, s: str) -> bool:
        import re
        return not re.match(r'.*LLL.*|.*A.*A.*', s)
    
    def checkRecord_str(self, s: str) -> bool:
        return s.find('A') == s.rfind('A') and 'LLL' not in s
    
    def checkRecord_str2(self, s: str) -> bool:
        return s.count('A') < 2 and s.count('LLL') == 0


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)

            sol = Solution()
            ret = sol.checkRecord(s)
            ret2 = sol.checkRecord_2(s)
            ret_r = sol.checkRecord_re(s)
            ret_r2 = sol.checkRecord_re2(s)
            ret_s = sol.checkRecord_str(s)
            ret_s2 = sol.checkRecord_str2(s)
            
            print(f"Solved by counting A's and consecutive L's:   {ret}")
            print(f"Solved by counting A's and consecutive L's 2: {ret2}")
            print(f"Solved using re's .findall():                 {ret_r}")
            print(f"Solved using re's .match():                   {ret_r2}")
            print(f"Solved using Python str methods:              {ret_s}")
            print(f"Solved using Python's .count() method:        {ret_s2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
