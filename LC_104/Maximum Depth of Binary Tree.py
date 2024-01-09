"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.
"""
import collections

from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def maxDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        q = collections.deque([root])
        while q:
            depth += 1
            for _ in range(len(q)):
                current = q.pop()
                
                if current.left:
                    q.appendleft(current.left)
                if current.right:
                    q.appendleft(current.right)
                    
        return depth
    
    def maxDepth_dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth_dfs(root.left),
                   self.maxDepth_dfs(root.right)) + 1


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret_bfs = sol.maxDepth_bfs(root)
            ret_dfs = sol.maxDepth_dfs(root)
            
            print(f"Solved using BFS: {ret_bfs}")
            print(f"Solved using DFS: {ret_dfs}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
