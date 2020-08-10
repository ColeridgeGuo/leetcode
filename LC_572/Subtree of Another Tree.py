"""
Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def isSubtree_recursive(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Time Complexity : O(m*n)
        Space Complexity : O(n)
        """
        
        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and \
                   isSameTree(p.left, q.left) and \
                   isSameTree(p.right, q.right)
        if not s:
            return False
        return isSameTree(s, t) or \
               self.isSubtree_recursive(s.left, t) or \
               self.isSubtree_recursive(s.right, t)
    
    def isSubtree_preorder(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Time complexity : O(m^2 + n^2 + m*n)
        Space complexity : O(max(m,n))
        """
        def preorder(p: TreeNode):
            if not p:
                return 'null'
            return f'#{p.val} {preorder(p.left)} {preorder(p.right)}'
        
        return preorder(t) in preorder(s)


def main():
    while True:
        try:
            line = input()
            s = stringToTreeNode(line)
            line = input()
            t = stringToTreeNode(line)
            
            sol = Solution()
            ret = sol.isSubtree_recursive(s, t)
            ret_p = sol.isSubtree_preorder(s, t)
            
            print(f"Solved by comparing subtrees recursively: {ret}")
            print(f"Solved by comparing preorder traversal:   {ret_p}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
