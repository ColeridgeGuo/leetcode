"""
Given two binary trees and imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString
    
    
class Solution:
    def mergeTrees_r(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees_r(t1.left, t2.left)
        t1.right = self.mergeTrees_r(t1.right, t2.right)
        return t1
    
    def mergeTrees_i(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        stack = [(t1, t2)]
        while stack:
            t = stack.pop()
            if t[0] and t[1]:
                t[0].val += t[1].val
                if not t[0].left:
                    t[0].left = t[1].left
                else:
                    stack.append((t[0].left, t[1].left))
                if not t[0].right:
                    t[0].right = t[1].right
                else:
                    stack.append((t[0].right, t[1].right))
        return t1


def main():
    while True:
        try:
            line = input()
            t1 = stringToTreeNode(line)
            t1_2 = stringToTreeNode(line)
            line = input()
            t2 = stringToTreeNode(line)
            t2_2 = stringToTreeNode(line)

            sol = Solution()
            ret_r = sol.mergeTrees_r(t1, t2)
            ret_i = sol.mergeTrees_i(t1_2, t2_2)
            
            out_r = treeNodeToString(ret_r)
            out_i = treeNodeToString(ret_i)
            print(f"Solved recursively: {out_r}")
            print(f"Solved iteratively: {out_i}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
