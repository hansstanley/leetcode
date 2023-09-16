from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
        self,
        head: Optional[ListNode],
        x: int,
    ) -> Optional[ListNode]:
        l1_head, l1_tail = None, None
        l2_head, l2_tail = None, None
        while head is not None:
            l_head, l_tail = (
                (l1_head, l1_tail)
                if head.val < x
                else (
                    l2_head,
                    l2_tail,
                )
            )
            if l_head is None:
                l_head = l_tail = head
            else:
                assert l_tail is not None
                l_tail.next = head
                l_tail = head
            if head.val < x:
                l1_head, l1_tail = l_head, l_tail
            else:
                l2_head, l2_tail = l_head, l_tail
            head = head.next
        if l1_tail is not None:
            l1_tail.next = l2_head
        if l2_tail is not None:
            l2_tail.next = None
        return l1_head or l2_head
