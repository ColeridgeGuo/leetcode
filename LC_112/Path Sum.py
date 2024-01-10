"""
"""
from common_funcs import TreeNode, stringToTreeNode, treeNodeToString


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

    def hasPathSum_iter(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, sum_ = stack.pop()
            if not node.left and not node.right:
                if sum_ == targetSum:
                    return True
            if node.left:
                stack.append((node.left, sum_ + node.left.val))
            if node.right:
                stack.append((node.right, sum_ + node.right.val))
        return False


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            targetSum = int(line)

            sol = Solution()
            ret = sol.hasPathSum(root, targetSum)
            ret2 = sol.hasPathSum_iter(root, targetSum)

            print(f"Solved recursively with DFS: {ret}")
            print(f"Solved iteratively with DFS: {ret2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
