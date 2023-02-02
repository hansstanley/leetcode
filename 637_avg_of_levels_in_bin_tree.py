from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        level = [root]
        while len(level) > 0:
            avg.append(sum([node.val for node in level]) / len(level))
            next_level = []
            for node in level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            level = next_level
        return avg