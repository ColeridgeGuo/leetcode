"""
    Given preorder and inorder traversal of a tree, construct the binary tree.
"""
from typing import List
from common_funcs import TreeNode, treeNodeToString, stringToList
        
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root_val = preorder.pop(0)  # the first element of preorder is the root
        idx = inorder.index(root_val)  # find index of root in inorder
        
        lsub_in = inorder[:idx]  # left children are to the left of root
        rsub_in = inorder[idx+1:]  # right children are to the right of root
        
        lsub_len = len(lsub_in)  # length of left subtree
        # As recursive calls pop root off of preorder, there's actually no need
        # to calculate preorder for left and right subtree, as in buildTree_2()
        lsub_pre = preorder[:lsub_len]  # preorder of left subtree
        rsub_pre = preorder[lsub_len:]  # preorder of right subtree
        
        lsub = self.buildTree(lsub_pre, lsub_in)
        rsub = self.buildTree(rsub_pre, rsub_in)
        root = TreeNode(root_val, lsub, rsub)
        return root

    def buildTree_2(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree_2(preorder, inorder[:ind])
            root.right = self.buildTree_2(preorder, inorder[ind + 1:])
            return root

    def buildTree_3(self, preorder, inorder):
        preorder_index = 0
        inorder_index_map = {x: i for i, x in enumerate(inorder)}

        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return
            root_val = preorder[preorder_index]
            preorder_index += 1
            lsub = helper(left, inorder_index_map[root_val]-1)
            rsub = helper(inorder_index_map[root_val]+1, right)
            return TreeNode(root_val, lsub, rsub)

        return helper(0, len(preorder)-1)


def main():
    while True:
        try:
            line = input()
            preorder = stringToList(line)
            preorder2 = stringToList(line)
            preorder3 = stringToList(line)
            line = input()
            inorder = stringToList(line)
            inorder2 = stringToList(line)
            inorder3 = stringToList(line)

            sol = Solution()
            ret = sol.buildTree(preorder, inorder)
            ret2 = sol.buildTree_2(preorder2, inorder2)
            ret3 = sol.buildTree_3(preorder3, inorder3)

            out = treeNodeToString(ret)
            out2 = treeNodeToString(ret2)
            out3 = treeNodeToString(ret3)
            print(out)
            print(out2)
            print(out3)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
