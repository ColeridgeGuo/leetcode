"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times. Note that k is guaranteed to
be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't
be input like 3a or 2[4].
"""
from common_funcs import stringToString
from typing import List, Deque


class Solution:
    def decodeString_stack(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = []
        for c in s:
            if c == '[':
                # start new repeated string by pushing the string before it and
                # its repeated times onto the stack, to be popped later when "]"
                # is encountered
                stack.append(curr_str[:])
                stack.append(curr_num)
                curr_str.clear()
                curr_num = 0
            elif c == ']':
                # finish repeated string by popping repeated times and previous
                # string off of the stack, repeat it, and append it
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            elif c.isdigit():
                # accumulate the number of times to repeat
                curr_num = curr_num * 10 + int(c)
            else:
                curr_str.append(c)
        return ''.join(curr_str)
    
    def decodeString_recur(self, s: str) -> str:
        from collections import deque
        queue = deque(s)
        
        def decode(q: Deque[str]) -> List[str]:
            sb = []
            num = 0
            while q:
                char = q.popleft()
                if char == '[':
                    # recursively call decode to process the next part w/i []
                    sub = decode(q)
                    sb.extend(sub * num)  # repeat string and append it
                    num = 0
                elif char == ']':
                    # break on seeing a ']' or at the end of the string
                    break
                elif char.isdigit():
                    # accumulate the number of times to repeat
                    num = num * 10 + int(char)
                else:
                    sb.append(char)
            return sb
        
        return ''.join(decode(queue))
    
    def decodeString_re(self, s: str) -> str:
        import re
        while '[' in s:
            s = re.sub(r'(\d+)\[(\w*)]', lambda m: int(m.group(1)) * m.group(2), s)
        return s


def main():
    while True:
        try:
            line = input()
            s = stringToString(line)
            
            sol = Solution()
            ret = sol.decodeString_stack(s)
            ret2 = sol.decodeString_recur(s)
            ret3 = sol.decodeString_re(s)
            
            print(f"Solved using a stack: {ret}")
            print(f"Solved recursively:   {ret2}")
            print(f"Solved using regex:   {ret3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
