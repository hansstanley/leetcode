# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, max_sum = self.traverse(root)
        return max_sum
    def traverse(self, root: Optional[TreeNode]):
        if not root: return 0, None
        l_partial, l_max = self.traverse(root.left)
        r_partial, r_max = self.traverse(root.right)
        c_partial = max(root.val, root.val + l_partial, root.val + r_partial)
        c_max = root.val
        if l_max is not None and r_max is not None:
            c_max = max(l_max, r_max, root.val + max(0, l_partial) + max(0, r_partial))
        elif l_max is not None:
            c_max = max(l_max, root.val + max(0, l_partial))
        elif r_max is not None:
            c_max = max(r_max, root.val + max(0, r_partial))
        return c_partial, c_max