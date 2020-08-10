"""
    Given a binary tree, return all root-to-leaf paths.
"""
from typing import List
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def binaryTreePaths_recursive(self, root: TreeNode) -> List[str]:
        answer = []
        if root:
            self.helper(root, "", answer)
        return answer
    
    def helper(self, root: TreeNode, path: str, answer: List[str]):
        if not root.left and not root.right:
            answer.append(f"{path}{root.val}")
            return
        if root.left:
            self.helper(root.left, f"{path}{root.val}->", answer)
        if root.right:
            self.helper(root.right, f"{path}{root.val}->", answer)

    def binaryTreePaths_iterative(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(f"{path}{node.val}")
            if node.right:
                stack.append((node.right, f"{path}{node.val}->"))
            if node.left:
                stack.append((node.left, f"{path}{node.val}->"))
        return res


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            
            sol = Solution()
            ret_recur = sol.binaryTreePaths_recursive(root)
            ret_iter = sol.binaryTreePaths_iterative(root)
            
            print(f"Solved recursively: {ret_recur}")
            print(f"Solved using DFS:   {ret_iter}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
