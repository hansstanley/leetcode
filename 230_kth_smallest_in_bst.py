from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _, res = self.dfs(root, k)
        return res
    def dfs(self, root: Optional[TreeNode], k: int, l_count = 0):
        if not root: return l_count, None
        i, kth = self.dfs(root.left, k, l_count)
        i += 1
        if kth is not None: return i, kth
        if k == i: return i, root.val
        j, kth = self.dfs(root.right, k, i)
        return j, kth
