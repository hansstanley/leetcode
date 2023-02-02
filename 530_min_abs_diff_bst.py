from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        _, _, diff = self.dfs(root)
        return diff
    def dfs(self, root: TreeNode):
        if not root.left and not root.right: return root.val, root.val, None
        l_min, l_max, l_diff = self.dfs(root.left) if root.left else (root.val, None, None)
        r_min, r_max, r_diff = self.dfs(root.right) if root.right else (None, root.val, None)
        min_diff = min([d for d in [
            l_diff,
            r_diff,
            root.val - l_max if l_max is not None else None,
            r_min - root.val if r_min is not None else None
        ] if d is not None])
        return l_min, r_max, min_diff