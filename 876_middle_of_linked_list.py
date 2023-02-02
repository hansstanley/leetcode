from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head)
            head = head.next
        return vals[len(vals) // 2 + (0 if len(vals) % 2 == 0 else 0)]