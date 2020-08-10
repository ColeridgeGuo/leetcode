"""
Given a binary tree, find the length of the longest path where each node in the
path has the same value. This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges
between them.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.LUP = 0
        
        def findLUP(node: TreeNode):
            if not node:
                return 0
            l_path = findLUP(node.left)
            r_path = findLUP(node.right)
            l_arrow = r_arrow = 0
            if node.left and node.val == node.left.val:
                l_arrow = l_path + 1
            if node.right and node.val == node.right.val:
                r_arrow = r_path + 1
            self.LUP = max(self.LUP, l_arrow + r_arrow)
            return max(l_arrow, r_arrow)
        
        findLUP(root)
        return self.LUP

    def longestUnivaluePath_2(self, root: TreeNode) -> int:
        self.LUP = 0
        
        def findLUP(node: TreeNode, parent_val: int):
            if not node:
                return 0
            left = findLUP(node.left, node.val)
            right = findLUP(node.right, node.val)
            self.LUP = max(self.LUP, left + right)
            return max(left, right) + 1 if node.val == parent_val else 0
        
        findLUP(root, None)
        return self.LUP


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret = sol.longestUnivaluePath(root)
            ret_2 = sol.longestUnivaluePath_2(root)
            
            print(ret)
            print(ret_2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
