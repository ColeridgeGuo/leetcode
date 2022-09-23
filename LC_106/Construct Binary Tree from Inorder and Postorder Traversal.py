"""
    Given inorder and postorder traversal of a tree, construct the binary tree.
"""
from typing import List
from common_funcs import TreeNode, treeNodeToString, stringToList


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root

    def buildTree_2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder_index = len(postorder)-1
        inorder_index_map = {x: i for i, x in enumerate(inorder)}

        def helper(left, right):
            nonlocal postorder_index
            if left > right:
                return
            root_val = postorder[postorder_index]
            postorder_index -= 1
            rsub = helper(inorder_index_map[root_val]+1, right)
            lsub = helper(left, inorder_index_map[root_val]-1)
            return TreeNode(root_val, lsub, rsub)

        return helper(0, len(postorder)-1)


def main():
    while True:
        try:
            line = input()
            inorder = stringToList(line)
            inorder2 = stringToList(line)
            line = input()
            postorder = stringToList(line)
            postorder2 = stringToList(line)

            ret = Solution().buildTree(inorder, postorder)
            ret2 = Solution().buildTree_2(inorder2, postorder2)

            out = treeNodeToString(ret)
            out2 = treeNodeToString(ret2)
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
