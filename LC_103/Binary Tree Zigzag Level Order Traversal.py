"""
Given the root of a binary tree, return the zigzag level order traversal of its 
nodes' values. (i.e., from left to right, then right to left for the next level 
and alternate between).
"""
from tkinter.tix import Tree
from typing import List, Optional
from common_funcs import TreeNode, listToString, stringToList, stringToTreeNode
from collections import deque


class Solution:
    def zigzagLevelOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        level = 0
        while queue:
            res.append([])
            for _ in range(len(queue)):
                if level % 2:  # odd level
                    node = queue.pop()
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                    res[level].append(node.val)
                else:  # even level
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    res[level].append(node.val)
            level += 1
        return res

    def zigzagLevelOrder_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(node: TreeNode, level: int):
            if level >= len(res):
                res.append(deque([node.val]))
            else:
                if level % 2:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        return res


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)

            sol = Solution()
            ret = sol.zigzagLevelOrder_bfs(root)
            ret2 = sol.zigzagLevelOrder_dfs(root)

            out = listToString(ret)
            out2 = listToString([list(row) for row in ret2])
            print(out)
            print(out2)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
