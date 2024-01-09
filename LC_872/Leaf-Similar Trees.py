"""
Consider all the leaves of a binary tree, from left to right order, the values
of those leaves form a leaf value sequence. Two binary trees are considered
leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2
are leaf-similar.
"""
import itertools
from typing import List

from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> List[int]:
            if not node.left and not node.right:
                return [node.val]
            leaves = []
            if node.left:
                leaves += dfs(node.left)
            if node.right:
                leaves += dfs(node.right)
            return leaves

        return dfs(root1) == dfs(root2)

    def leafSimilar_2(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))


def main():
    while True:
        try:
            line = input()
            root1 = stringToTreeNode(line)
            line = input()
            root2 = stringToTreeNode(line)

            sol = Solution()
            ret = sol.leafSimilar(root1, root2)
            ret2 = sol.leafSimilar_2(root1, root2)

            print(ret)
            print(ret2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
