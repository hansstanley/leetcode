from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], tail: Optional[ListNode] = None) -> Optional[ListNode]:
        if not head: return tail
        next_head, head.next = head.next, tail
        return self.reverseList(next_head, head)