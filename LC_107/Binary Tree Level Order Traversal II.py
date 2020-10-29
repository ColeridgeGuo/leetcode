"""
Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).
"""
from typing import List
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def levelOrderBottom_iterative(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        from collections import deque
        traversal = deque()
        q = deque()
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                c = q.popleft()
                
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                level.append(c.val)
            traversal.appendleft(level)
            
        return list(traversal)
    
    def levelOrderBottom_recursive(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        res = deque()
        self.dfs(root, 0, res)
        return list(res)

    def dfs(self, root, level, res):
        if root:
            if len(res) <= level:
                res.appendleft([])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret_iter = sol.levelOrderBottom_iterative(root)
            ret_recur = sol.levelOrderBottom_recursive(root)
            
            print(f"Solved iteratively: {ret_iter}")
            print(f"Solved recursively: {ret_recur}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
