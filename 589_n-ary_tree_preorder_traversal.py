from typing import List


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        traversal = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            traversal.append(curr.val)
            if curr.children: stack.extend(reversed(curr.children))
        return traversal