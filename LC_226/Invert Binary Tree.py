"""
    Invert a binary tree.
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString
        
        
class Solution:
    def invertTree_recursive(self, root: TreeNode) -> TreeNode:
        """
            Time Complexity: O(n)
            Space Complexity: O(h) ∈ O(n), h is the height of the tree
        """
        if not root:
            return root
        root.left, root.right = self.invertTree_recursive(root.right), self.invertTree_recursive(root.left)
        return root
    
    def invertTree_iterative(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        queue = [root]
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


def main():
    while True:
        try:
            line = input()
            root1 = stringToTreeNode(line)
            root2 = stringToTreeNode(line)
            
            sol = Solution()
            ret_recur = sol.invertTree_recursive(root1)
            ret_iter = sol.invertTree_iterative(root2)
            
            out_recur = treeNodeToString(ret_recur)
            out_iter = treeNodeToString(ret_iter)
            print(f"Solved recursively: {out_recur}")
            print(f"Solved iteratively: {out_iter}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
