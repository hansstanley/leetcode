from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        temp, last, n = head, head, 0
        while temp is not None:
            n += 1
            last = temp
            temp = temp.next
        skip = n - (k % n)
        if skip in {0, n}:
            return head
        chop = head
        for _ in range(1, skip):
            assert chop is not None
            chop = chop.next
        first = chop.next
        last.next = head
        chop.next = None
        return first
