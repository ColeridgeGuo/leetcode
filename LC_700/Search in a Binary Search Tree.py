"""
Given the root node of a binary search tree and a value. You need to find the
node in the BST that the node's value equals the given value. Return the subtree
rooted with that node. If such node doesn't exist, you should return NULL.
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def searchBST_recursive(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        if val < root.val:
            return self.searchBST_recursive(root.left, val)
        elif val > root.val:
            return self.searchBST_recursive(root.right, val)
        return root

    def searchBST_iterative(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            n = int(line)
            
            sol = Solution()
            ret_r = sol.searchBST_recursive(root, n)
            ret_i = sol.searchBST_iterative(root, n)
            
            out_r = treeNodeToString(ret_r)
            out_i = treeNodeToString(ret_i)
            print(f"Solved recursively: {out_r}")
            print(f"Solved iteratively: {out_i}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
