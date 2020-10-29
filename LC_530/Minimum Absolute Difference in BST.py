"""
Given a binary search tree with non-negative values, find the minimum absolute
difference between values of any two nodes.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        inorder = self.inorder(root)
        min_diff = float('inf')
        for i in range(len(inorder) - 1):
            min_diff = min(min_diff, abs(inorder[i] - inorder[i + 1]))
        return min_diff
    
    def inorder(self, node: TreeNode) -> list:
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
    
    # instance variables for method 2
    min_diff = float('inf')
    prev = None
    
    def getMinimumDifference_2(self, root: TreeNode) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        self.inorder_2(root)
        return self.min_diff
    
    def inorder_2(self, node: TreeNode) -> None:
        if node:
            self.inorder_2(node.left)
            if self.prev:
                self.min_diff = min(self.min_diff, node.val - self.prev.val)
            self.prev = node
            self.inorder_2(node.right)

    def getMinimumDifference_3(self, root):
        def mindiff(root, lo, hi):
            if not root:
                return float('inf')
            lmin = mindiff(root.left, lo, root.val)
            rmin = mindiff(root.right, root.val, hi)
            return min(root.val - lo, hi - root.val, lmin, rmin)
        
        return mindiff(root, float('-inf'), float('inf'))


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            root2 = stringToTreeNode(line)
            root3 = stringToTreeNode(line)

            sol = Solution()
            ret = sol.getMinimumDifference(root)
            ret2 = sol.getMinimumDifference_2(root2)
            ret3 = sol.getMinimumDifference_3(root3)
            
            out = str(ret)
            out2 = str(ret2)
            out3 = str(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
