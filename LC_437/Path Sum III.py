"""
Given the root of a binary tree and an integer targetSum, return the number of
paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).
"""
import collections

from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        Store the prefix sum (cumulative sum from root up to current node) into
        hashmap. If curr_sum-target exists in the map, then a path that sums up
        to target must exist.
        """
        prefix_sum = collections.Counter({0: 1})

        def backtrack(node: TreeNode | None, curr_sum: int) -> int:
            if not node:
                return 0
            curr_sum += node.val
            # (curr_sum - targetSum) exists in prefix_sum means there is a path
            # that sums up to targetSum, hence we increment the answer
            res = prefix_sum[curr_sum - targetSum]
            prefix_sum[curr_sum] += 1
            res += (backtrack(node.left, curr_sum) +
                    backtrack(node.right, curr_sum))
            prefix_sum[curr_sum] -= 1
            return res

        return backtrack(root, 0)


def main():
    while True:
        try:
            line = input()
            root = stringToTreeNode(line)
            line = input()
            s = int(line)
            
            sol = Solution()
            ret = sol.pathSum(root, s)
            
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
