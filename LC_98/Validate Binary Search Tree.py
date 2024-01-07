"""
Given the root of a binary tree, determine if it is a valid binary search tree.

A valid BST is defined as follows:

- The left subtree of a node contains only keys less than the node's key.
- The right subtree of a node contains only keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return (dfs(node.left, min_val, node.val) and
                    dfs(node.right, node.val, max_val))

        return dfs(root, float('-inf'), float('inf'))

    def isValidBST_iter(self, root: TreeNode | None) -> bool:
        stack = []
        prev, curr = None, root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev and prev.val >= curr.val:
                return False
            prev = curr
            curr = curr.right
        return True


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.isValidBST(root)
            ret2 = sol.isValidBST_iter(root)

            out = str(ret)
            out2 = str(ret2)
            print(f"Solved with recursive dfs :              {out}")
            print(f'Solved with iterative inorder traversal: {out2}')
        except StopIteration:
            break


if __name__ == '__main__':
    main()
