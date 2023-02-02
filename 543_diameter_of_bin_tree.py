from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.dfs(root)
        return diameter
    def dfs(self, root: Optional[TreeNode]):
        if not root: return 0, 0
        l_depth, l_max = self.dfs(root.left)
        r_depth, r_max = self.dfs(root.right)
        return max(l_depth, r_depth) + 1, max(l_max, r_max, l_depth + r_depth)