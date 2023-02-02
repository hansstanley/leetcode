from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = str(root.val)
        if root.left: res += f'({self.tree2str(root.left)})'
        if root.right:
            res += '()' if not root.left else ''
            res += f'({self.tree2str(root.right)})'
        return res
        if not root.left and not root.right: return str(root.val)
        l_str = f'({self.tree2str(root.left)})' if root.left else ''
        r_str = f'({self.tree2str(root.right)})' if root.right else ''
        return f'{root.val}{l_str}{r_str}'
        