"""
Given the root of a binary tree and an integer targetSum, return all
root-to-leaf paths where the sum of the node values in the path equals
targetSum. Each path should be returned as a list of the node values, not node
references.

A root-to-leaf path is a path starting from the root and ending at a leaf node.
"""
from typing import List
from common_funcs import TreeNode, stringToTreeNode, listToString


class Solution:
    def pathSum_r(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        ans = []

        def backtrack(node: TreeNode | None, path: List[int], path_sum: int):
            if not node:
                return
            path.append(node.val)
            new_sum = path_sum + node.val
            if not node.left and not node.right and new_sum == targetSum:
                ans.append(path[:])
            backtrack(node.left, path, new_sum)
            backtrack(node.right, path, new_sum)
            path.pop()

        backtrack(root, [], 0)
        return ans

    def pathSum_i(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        stack = [(root, [root.val], root.val)]
        while stack:
            node, path, path_sum = stack.pop()
            if not node.left and not node.right and path_sum == targetSum:
                ans.append(path)
            if node.left:
                stack.append((node.left, path + [node.left.val],
                              path_sum + node.left.val))
            if node.right:
                stack.append((node.right, path + [node.right.val],
                              path_sum + node.right.val))
        return ans


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            targetSum = int(line)

            sol = Solution()
            ret = sol.pathSum_r(root, targetSum)
            ret2 = sol.pathSum_i(root, targetSum)

            out = listToString(ret)
            out2 = listToString(ret2)
            print(f"Solved recursively with DFS: {out}")
            print(f"Solved iteratively with DFS: {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
