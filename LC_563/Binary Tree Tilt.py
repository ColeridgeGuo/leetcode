"""
Given a binary tree, return the tilt of the whole tree. The tilt of a tree node
is defined as the absolute difference between the sum of all left subtree node
values and the sum of all right subtree node values. Null node has tilt 0. The
tilt of the whole tree is defined as the sum of all nodes' tilt.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    tilt_total = 0
    
    def findTilt(self, root: TreeNode) -> int:
        
        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            lsum, rsum = helper(node.left), helper(node.right)
            self.tilt_total += abs(lsum - rsum)
            return node.val + lsum + rsum
        
        helper(root)
        return self.tilt_total


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.findTilt(root)
            
            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
