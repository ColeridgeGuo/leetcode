"""
Given the root of a binary tree, flatten the tree into a "linked list":

- Use the same TreeNode class where the right child pointer points to the next 
node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the 
binary tree.
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Perform a preorder traversal of the tree and store the values of each 
        node in an array and modify root's children with the values to flatten.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []

        def preorder(root: TreeNode) -> None:
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        curr = root
        for i in range(1, len(res)):
            curr.left, curr.right = None, TreeNode(res[i])
            curr = curr.right

    def flatten_2(self, root: TreeNode) -> None:
        """
        Use reverse preorder traversal on the tree: process right subtree then 
        left subtree; keep track of prev which is the flattened right subtree to 
        append to current node; remove left child; update prev
        Time Complexity: 
        Space Complexity: 
        """
        prev = None

        def preorder(node: TreeNode) -> None:
            nonlocal prev
            if not node:
                return
            preorder(node.right)
            preorder(node.left)
            node.right, node.left = prev, None
            prev = node

        preorder(root)


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            root2 = stringToTreeNode(line)

            sol = Solution()
            sol.flatten(root)
            sol.flatten_2(root2)

            out = treeNodeToString(root)
            out2 = treeNodeToString(root2)
            print(f"Solved w/ O(n) space:     {out}")
            print(f"Solved w/ constant space: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
