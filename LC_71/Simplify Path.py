"""
Given a string path, which is an absolute path (starting with a slash '/') to a 
file or directory in a Unix-style file system, convert it to the simplified 
canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a 
double period '..' refers to the directory up a level, and any multiple 
consecutive slashes (i.e. '//') are treated as a single slash '/'. 
For this problem, any other format of periods such as '...' are treated as 
file/directory names.

The canonical path should have the following format:
- The path starts with a single slash '/'.
- Any two directories are separated by a single slash '/'.
- The path does not end with a trailing '/'.
- The path only contains the directories on the path from the root directory to 
the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.
"""
from common_funcs import stringToString, stringToString_out


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for dir in path.split('/'):
            if not dir or dir == '.':
                # ignore empty directory or same directory (.)
                continue
            elif dir == '..':
                # go up one level by popping off stack
                if stack:
                    stack.pop()
            else:
                # go down one level by appending to stack
                stack.append(dir)
        return '/' + '/'.join(stack)


def main():
    while True:
        try:
            line = input()
            path = stringToString(line)

            sol = Solution()
            ret = sol.simplifyPath(path)

            out = stringToString_out(ret)
            print(f"Solved using stack: {out}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
