"""
Given an inorder traversal of a binary tree, build the tree for which all parent 
values are greater than child values (like a max-heap not necessarily balanced)
"""
from typing import List
from common_funcs import stringToList, TreeNode, treeNodeToString


class Solution:
    def constructMaximumBinaryTree_recur(self, nums: List[int]) -> TreeNode:
        """
        Find the maximum number in nums which has to be the root for the current 
        subtree (according to properties of aCartesian tree), recursively build 
        left and right subtrees from numbers to the left and the right of max 
        (according to properties of inorder traversal).
        Time Complexity: O(n^2)
        """
        if nums:
            root_val = max(nums)
            root_idx = nums.index(root_val)
            left = self.constructMaximumBinaryTree_recur(nums[:root_idx])
            right = self.constructMaximumBinaryTree_recur(nums[root_idx+1:])
            return TreeNode(root_val, left, right)
    
    def constructMaximumBinaryTree_iter(self, nums: List[int]) -> TreeNode:
        """
        Inorder traversal guarantees that anything to the left of the root is in 
        the left subtree and the same for right subtree for any subtree. We scan 
        the traversal from left to right, decreasing numbers become right 
        subtrees (parent > child); a larger number would be a new subtree with 
        its left child being all the numbers less than it.
        Time Complexity: O(n)
        """
        stack = []
        for n in nums:
            curr = TreeNode(n)
            while stack and stack[-1].val < n:
                # pop off all nodes smaller than curr and make them left child
                curr.left = stack.pop()
            if stack:
                # the last node on stack not popped off is the root for curr
                # subtree because it must be greater than curr
                stack[-1].right = curr
            stack.append(curr)  # push curr onto stack
        return stack[0] # 1st node is the largest hence the root

def main():
    while True:
        try:
            line = input()
            nums = stringToList(line)

            sol = Solution()
            ret = sol.constructMaximumBinaryTree_recur(nums)
            ret2 = sol.constructMaximumBinaryTree_iter(nums)

            out = treeNodeToString(ret)
            out2 = treeNodeToString(ret2)
            print(f"Solved recursively in quadratic time: {out}")
            print(f"Solved iteratively in linear time:    {out2}")
        except StopIteration:
            break


if __name__ == '__main__':
    main()
