"""
Given the root of a binary tree, return the level order traversal of its nodes'
values. (i.e., from left to right, level by level).
"""
from collections import deque
from typing import List

from common_funcs import TreeNode, listToString, stringToTreeNode



class Solution:

    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque([root])
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.levelOrder(root)

            out = listToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
