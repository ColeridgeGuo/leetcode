"""
Given the root of a binary tree, return the inorder traversal
"""
from typing import List
from common_funcs import stringToTreeNode, TreeNode, listToString


class Solution:
    def inorderTraversal_recur(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        res += self.inorderTraversal_recur(root.left)
        res += [root.val]
        res += self.inorderTraversal_recur(root.right)
        return res

    def inorderTraversal_iter(self, root: TreeNode) -> List[int]:
        res, stack, curr = [], [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def inorderTraversal_morris(self, root: TreeNode) -> List[int]:
        res = []
        curr, prev = root, None
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr
                curr.left, curr = None, curr.left
        return res


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            root2 = stringToTreeNode(line)
            root3 = stringToTreeNode(line)

            sol = Solution()
            ret = sol.inorderTraversal_recur(root)
            ret2 = sol.inorderTraversal_iter(root2)
            ret3 = sol.inorderTraversal_morris(root3)

            out = listToString(ret)
            out2 = listToString(ret2)
            out3 = listToString(ret3)
            print(f"Solved recursively:         {out}")
            print(f"Solved iteratively:         {out2}")
            print(f"Solved using Morris method: {out3}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
