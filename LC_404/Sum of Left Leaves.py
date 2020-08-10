"""
Find the sum of all left leaves in a given binary tree.
"""
from common_funcs import TreeNode, stringToTreeNode
    

class Solution:
    def sumOfLeftLeaves_helper(self, root: TreeNode) -> int:
        """
            Use a helper function to determine whether the current node is left
            or right.
        """
        def helper(isLeft, root: TreeNode) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if isLeft else 0
            return helper(True, root.left) + helper(False, root.right)
        return helper(False, root)
    
    def sumOfLeftLeaves_recursive(self, root: TreeNode) -> int:
        if not root:
            return 0
        # if left child is leaf, return its val with right child's sum
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves_recursive(root.right)
        return self.sumOfLeftLeaves_recursive(root.left) + self.sumOfLeftLeaves_recursive(root.right)
    
    def sumOfLeftLeaves_iterative(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val  # if left child is leaf
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret_hp = sol.sumOfLeftLeaves_helper(root)
            ret_rc = sol.sumOfLeftLeaves_recursive(root)
            ret_it = sol.sumOfLeftLeaves_iterative(root)
            
            print(f"Solved with helper function: {ret_hp}")
            print(f"Solved recursively:          {ret_rc}")
            print(f"Solved iteratively:          {ret_it}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
