from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        n1, n2 = head, head.next
        if n2 is None:
            return n1
        n3 = self.swapPairs(n2.next)
        n2.next = n1
        n1.next = n3
        return n2
