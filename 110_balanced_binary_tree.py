from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, res = self.traverse(root)
        return res
    def traverse(self, root: Optional[TreeNode]):
        if not root: return 0, True
        l_height, l_bal = self.traverse(root.left)
        r_height, r_bal = self.traverse(root.right)
        return max(l_height, r_height) + 1, l_bal and r_bal and abs(l_height - r_height) <= 1