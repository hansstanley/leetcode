from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res

        is_zag = False
        level = [root]
        while len(level) > 0:
            vals = [node.val for node in level]
            if is_zag: vals.reverse()
            res.append(vals)
            next_level = []
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
            is_zag = not is_zag
        return res