"""
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return 0


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            s = int(line)
            
            sol = Solution()
            ret = sol.pathSum(root, s)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
