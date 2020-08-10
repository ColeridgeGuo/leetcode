"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    while True:
        try:
            line = input()
            p = stringToTreeNode(line)
            line = input()
            q = stringToTreeNode(line)
            
            ret = Solution().isSameTree(p, q)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
