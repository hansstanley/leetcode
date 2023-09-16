from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.makeTree(1, n)

    def makeTree(self, lo: int, hi: int) -> List[Optional[TreeNode]]:
        if lo > hi:
            return [None]
        nodes: List[Optional[TreeNode]] = []
        for i in range(lo, hi + 1):
            nodes_left = self.makeTree(lo, i - 1)
            nodes_right = self.makeTree(i + 1, hi)
            for nl in nodes_left:
                for nr in nodes_right:
                    nodes.append(TreeNode(i, nl, nr))
        return nodes
