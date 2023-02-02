from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: return []
        if not root.left and not root.right:
            return [[root.val]] if root.val == targetSum else []
        l_paths = self.pathSum(root.left, targetSum - root.val)
        r_paths = self.pathSum(root.right, targetSum - root.val)
        return [[root.val] + p for p in l_paths + r_paths]