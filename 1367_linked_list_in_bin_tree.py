from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False
        return self.traverse(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    def traverse(self, curr_head: Optional[ListNode], curr_root: Optional[TreeNode]) -> bool:
        if not curr_head: return True
        if not curr_root: return False
        return curr_head.val == curr_root.val and \
            (self.traverse(curr_head.next, curr_root.left) or self.traverse(curr_head.next, curr_root.right))
    def traverse1(self, curr_head: Optional[ListNode], curr_root: Optional[TreeNode], head: ListNode) -> bool:
        if not curr_head: return True
        if not curr_root: return False
        cont_match = curr_root.val == curr_head.val and \
            (self.traverse(curr_head.next, curr_root.left, head) or self.traverse(curr_head.next, curr_root.right, head))
        if cont_match: return cont_match
        init_match = curr_root.val == head.val and \
            (self.traverse(head.next, curr_root.left, head) or self.traverse(head.next, curr_root.right, head))
        if init_match: return init_match
        next_match = self.traverse(head, curr_root.left, head) or self.traverse(head, curr_root.right, head)
        return next_match