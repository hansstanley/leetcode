from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode]):
            if not node: return 0, 0
            l_rob, l_not = traverse(node.left)
            r_rob, r_not = traverse(node.right)
            c_rob = node.val + l_not + r_not
            c_not = max(l_rob, l_not) + max(r_rob, r_not)
            return c_rob, c_not
        return max(traverse(root))