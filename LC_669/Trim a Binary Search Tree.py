"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). You might need
to change the root of the tree, so the result should return the new root of the
trimmed binary search tree.
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def trimBST_recursive(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return root
        elif root.val > R:
            return self.trimBST_recursive(root.left, L, R)
        elif root.val < L:
            return self.trimBST_recursive(root.right, L, R)
        else:
            root.left = self.trimBST_recursive(root.left, L, R)
            root.right = self.trimBST_recursive(root.right, L, R)
            return root
        
    def trimBST_iterative(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return root
        # find a valid root
        while root.val < L or root.val > R:
            if root.val < L:
                root = root.right
            if root.val > R:
                root = root.left
                
        dummy = root
        # remove the invalid nodes from left subtree.
        while dummy:
            while dummy.left and dummy.left.val < L:
                dummy.left = dummy.left.right
                # if left child smaller than L, keep the right subtree of it.
            dummy = dummy.left
            
        dummy = root
        # remove the invalid nodes from right subtree.
        while dummy:
            while dummy.right and dummy.right.val > R:
                dummy.right = dummy.right.left
                # if right child greater than R, keep the left subtree of it.
            dummy = dummy.right
        return root
    
    def trimBST_iterative_dfs(self, root: TreeNode, L: int, R: int):
        if not root:
            return root
        # find a valid root
        while root.val < L or root.val > R:
            if root.val < L:
                root = root.right
            if root.val > R:
                root = root.left
        stack = [root]
        while stack:
            node = stack[-1]
            if not node:
                stack.pop()
                continue
            update = 0
            if node.left and node.left.val < L:
                node.left = node.left.right
                update = 1
            if node.right and node.right.val > R:
                node.right = node.right.left
                update = 1
            if not update:
                stack.pop()
                stack.append(node.left)
                stack.append(node.right)
        return root


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            root1 = stringToTreeNode(line)
            root2 = stringToTreeNode(line)
            line = input()
            L = int(line)
            line = input()
            R = int(line)
            
            sol = Solution()
            ret_r = sol.trimBST_recursive(root, L, R)
            ret_i = sol.trimBST_iterative(root1, L, R)
            ret_id = sol.trimBST_iterative_dfs(root2, L, R)
            
            out = treeNodeToString(ret_r)
            out_i = treeNodeToString(ret_i)
            out_id = treeNodeToString(ret_id)
            print(f"Solved recursively:          {out}")
            print(f"Solved iteratively:          {out_i}")
            print(f"Solved iteratively with DFS: {out_id}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
