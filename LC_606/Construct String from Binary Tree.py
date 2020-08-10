"""
You need to construct a string consists of parenthesis and integers from a
binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". And you
need to omit all the empty parenthesis pairs that don't affect the one-to-one
mapping relationship between the string and the original binary tree.
"""
from common_funcs import TreeNode, stringToTreeNode


class Solution:
    def tree2str_r(self, t: TreeNode) -> str:
        if not t:
            return ''
        if not t.left and not t.right:
            return f'{t.val}'
        if not t.right:
            return f'{t.val}({self.tree2str_r(t.left)})'
        return f'{t.val}({self.tree2str_r(t.left)})({self.tree2str_r(t.right)})'
    
    def tree2str_r2(self, t: TreeNode) -> str:
        if not t:
            return ''
        res = [f'{t.val}']
        if t.left:
            res.append(f'({self.tree2str_r2(t.left)})')
        if t.right:
            if not t.left:
                res.append('()')
            res.append(f'({self.tree2str_r2(t.right)})')
        return ''.join(res)
    
    def tree2str_i(self, t: TreeNode) -> str:
        if not t:
            return ''
        stack, res, visited = [t], [], set()
        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                res.append(')')
            else:
                visited.add(node)
                res.append(f'({node.val}')
                if not node.left and node.right:
                    res.append('()')
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return ''.join(res)[1:-1]


def main():
    while True:
        try:
            line = input()
            t = stringToTreeNode(line)

            sol = Solution()
            ret_r = sol.tree2str_r(t)
            ret_r2 = sol.tree2str_r2(t)
            ret_i = sol.tree2str_i(t)
            
            print(f'Solved recursively:   {ret_r}')
            print(f'Solved recursively 2: {ret_r2}')
            print(f'Solved iteratively:   {ret_i}')
        except StopIteration:
            break


if __name__ == '__main__':
    main()
