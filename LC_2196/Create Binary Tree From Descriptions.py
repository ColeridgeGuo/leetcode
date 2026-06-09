"""
You are given a 2D integer array descriptions where descriptions[i] =
[parenti, childi, isLefti] indicates that parenti is the parent of childi in a
binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.

Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
"""
from typing import List, Optional

from common_funcs import TreeNode, stringToList, treeNodeToString


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)

        for parent, _, _ in descriptions:
            if parent not in children:
                root = nodes[parent]
                return root
        return None


def main():
    while True:
        try:
            line = input()
            descriptions = stringToList(line)

            sol = Solution()
            root = sol.createBinaryTree(descriptions)

            out = treeNodeToString(root)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
