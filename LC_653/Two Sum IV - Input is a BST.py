"""
Given a Binary Search Tree and a target number, return true if there exist two
elements in the BST such that their sum is equal to the given target.
"""
from common_funcs import TreeNode, stringToTreeNode
    
    
class Solution:
    def findTarget_iterative(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        stack, hashset = [root], set()
        while stack:
            node = stack.pop()
            if k - node.val in hashset:
                return True
            else:
                hashset.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    
    def findTarget_recursive(self, root: TreeNode, k: int) -> bool:
        hashset = set()
        
        def helper(node: TreeNode, k: int) -> bool:
            if not node:
                return False
            if k - node.val in hashset:
                return True
            hashset.add(node.val)
            return helper(node.left, k) or helper(node.right, k)
        
        return helper(root, k)
    
    def findTarget_inorder(self, root: TreeNode, k: int) -> bool:
        traversal = []
        
        def inorder(root: TreeNode):
            if root:
                inorder(root.left)
                traversal.append(root.val)
                inorder(root.right)
                
        inorder(root)
        l, r = 0, len(traversal) - 1
        while l < r:
            s = traversal[l] + traversal[r]
            if s == k:
                return True
            elif s < k:
                l += 1
            else:
                r -= 1
        return False


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            k = int(line)
            
            sol = Solution()
            ret_i = sol.findTarget_iterative(root, k)
            ret_r = sol.findTarget_recursive(root, k)
            ret_in = sol.findTarget_inorder(root, k)
            
            print(f"Solved iteratively:            {ret_i}")
            print(f"Solved recursively:            {ret_r}")
            print(f"Solved with inorder traversal: {ret_in}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
