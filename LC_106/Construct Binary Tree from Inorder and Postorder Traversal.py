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


def main():
    while True:
        try:
            line = input()
            inorder = stringToList(line)
            line = input()
            postorder = stringToList(line)
            
            ret = Solution().buildTree(inorder, postorder)
            
            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
