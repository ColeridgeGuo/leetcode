"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follows:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current
    node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1.
(A single node has a length of 0).
Return the longest ZigZag path contained in that tree.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    ans = 0

    def longestZigZag(self, root: TreeNode | None) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def dfs(node: TreeNode | None, from_left: bool, step: int):
            if not node:
                return
            self.ans = max(self.ans, step)
            if from_left:  # current node is a left subtree
                dfs(node.left, True, 1)
                dfs(node.right, False, step + 1)
            else:
                dfs(node.left, True, step + 1)
                dfs(node.right, False, 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.ans


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.longestZigZag(root)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
