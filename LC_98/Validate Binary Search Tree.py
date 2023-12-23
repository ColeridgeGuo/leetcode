"""
"""
from typing import Optional
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, minVal, maxVal):
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)

        return dfs(root, float('-inf'), float('inf'))

    def isValidBST_iter(self, root: Optional[TreeNode]) -> bool:
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