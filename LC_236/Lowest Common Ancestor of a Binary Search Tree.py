"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in
the tree.
Note:
- All the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree.
"""
from common_funcs import TreeNode, stringToTreeNode_pq


class Solution:
    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        """
        If p and q are both found in left and right subtrees, then the current
        node is the LCA. Otherwise, since all nodes' values are unique and that
        p and q are guaranteed to exist, if only one is found, then the other
        one must be a descendant of it, thus returning it directly as it is the
        LCA for both.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root in (None, p, q):
            return root
        lca_left = self.lca(root.left, p, q)
        lca_right = self.lca(root.right, p, q)
        if lca_left and lca_right:
            return root
        return lca_left or lca_right
        
    def lca_2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Perform DFS on the tree and store parent info on each node in a map.
        Put all of p's parents in a set and go up on q's ancestors to find LCA.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = [root]

        # Dictionary for parent pointers
        parents = {root: None}
        
        # Iterate until we find both the nodes p and q
        while not (p in parents and q in parents):
            curr = stack.pop()
            
            # While traversing the tree, keep saving the parent pointers.
            if curr.left:
                stack.append(curr.left)
                parents[curr.left] = curr
            if curr.right:
                stack.append(curr.right)
                parents[curr.right] = curr
                
        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parents[p]
            
        # The first ancestor of q that appears in p's ancestors is their LCA
        while q not in ancestors:
            q = parents[q]
        return q


def main():
    while True:
        try:
            line = input()
            p_val = int(input())
            q_val = int(input())
            root, p, q = stringToTreeNode_pq(line, p_val, q_val)
            
            sol = Solution()
            ret_r = sol.lca(root, p, q)
            ret_i = sol.lca_2(root, p, q)
            
            print(f"LCA found recursively: {ret_r}")
            print(f"LCA found iteratively: {ret_i}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
