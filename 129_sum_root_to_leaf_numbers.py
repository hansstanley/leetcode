from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], num = 0) -> int:
        if not root: return 0
        next_num = num * 10 + root.val
        if not root.left and not root.right: return next_num
        l_sum = self.sumNumbers(root.left, next_num)
        r_sum = self.sumNumbers(root.right, next_num)
        return l_sum + r_sum