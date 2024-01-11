"""
Given the root of a binary tree, find the maximum value v for which there exist
different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any
child of a is an ancestor of b.
"""
from typing import Tuple

from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:

        def dfs(node: TreeNode | None, max_: int, min_: int) -> int:
            # max and min values we have seen on our way down to node
            if not node:
                # update the max difference up all ancestors
                return max_ - min_
            max_ = max(max_, node.val)  # if current node is greater than max
            min_ = min(min_, node.val)  # if current node is less than min
            # return the max different down to both children
            return max(dfs(node.left, max_, min_), dfs(node.right, max_, min_))

        return dfs(root, root.val, root.val)


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.maxAncestorDiff(root)

            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
