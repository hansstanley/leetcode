from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> Optional[TreeNode]:
        if len(preorder) == len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        preorder_left = preorder[1 : 1 + root_idx]
        preorder_right = preorder[1 + root_idx :]
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1 :]
        node_left = self.buildTree(preorder_left, inorder_left)
        node_right = self.buildTree(preorder_right, inorder_right)
        root.left, root.right = node_left, node_right
        return root
