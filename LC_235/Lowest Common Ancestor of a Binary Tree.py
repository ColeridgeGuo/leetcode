"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.
Note:
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def lowestCommonAncestor_recursive(self,
                                       root: 'TreeNode',
                                       p: 'TreeNode',
                                       q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_recursive(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_recursive(root.right, p, q)
        else:
            return root
        
    def lowestCommonAncestor_iterative(self,
                                       root: 'TreeNode',
                                       p: 'TreeNode',
                                       q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            p = TreeNode(int(line))
            line = input()
            q = TreeNode(int(line))
            
            sol = Solution()
            ret_recur = sol.lowestCommonAncestor_recursive(root, p, q)
            ret_iter = sol.lowestCommonAncestor_iterative(root, p, q)
            
            print(f"LCA found recursively: {ret_recur.val}")
            print(f"LCA found iteratively: {ret_iter.val}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
