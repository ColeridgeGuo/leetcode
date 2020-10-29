"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def isSymmetric_iterative(self, root: TreeNode) -> bool:
        from collections import deque
        q = deque()
        q.append(root)
        q.append(root)
        
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
            
        return True

    def isSymmetric_recursive(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.isMirror(t1.right, t2.left) and self.isMirror(t1.left,
                                                                  t2.right)


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret_iter = sol.isSymmetric_iterative(root)
            ret_recur = sol.isSymmetric_recursive(root)
            
            print(ret_iter)
            print(ret_recur)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
