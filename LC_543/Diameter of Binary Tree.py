"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    diameter = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.findDiameter(root)
        return self.diameter
    
    def findDiameter(self, node: TreeNode) -> int:
        if not node:
            return 0
        lpath = self.findDiameter(node.left)
        rpath = self.findDiameter(node.right)
        self.diameter = max(self.diameter, lpath + rpath)
        return max(lpath, rpath) + 1


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.diameterOfBinaryTree(root)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
