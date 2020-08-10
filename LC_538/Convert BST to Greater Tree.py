"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus sum of all keys
greater than the original key in BST.
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString
    
    
class Solution:
    greater = 0
        
    def convertBST_recursive(self, root: TreeNode) -> TreeNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root:
            self.convertBST_recursive(root.right)
            self.greater += root.val
            root.val = self.greater
            self.convertBST_recursive(root.left)
        return root

    def convertBST_iterative(self, root: TreeNode) -> TreeNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        total = 0
    
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
        
            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left
        return root

    def convertBST_morris(self, root: TreeNode) -> TreeNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def get_successor(node):
            """
            Get the node with the smallest value greater than this one.
            """
            succ = node.right
            while succ.left and succ.left is not node:
                succ = succ.left
            return succ
        
        total = 0
        node = root
        while node:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                succ = get_successor(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            root2 = stringToTreeNode(line)
            root3 = stringToTreeNode(line)

            sol = Solution()
            ret_r = sol.convertBST_recursive(root)
            ret_i = sol.convertBST_iterative(root2)
            ret_m = sol.convertBST_morris(root3)
            
            out_r = treeNodeToString(ret_r)
            out_i = treeNodeToString(ret_i)
            out_m = treeNodeToString(ret_m)
            print(f"Solved with reverse-inorder traversal recursively: {out_r}")
            print(f"Solved with reverse-inorder traversal iteratively: {out_i}")
            print(f"Solved with Morris inorder traversal:              {out_m}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
