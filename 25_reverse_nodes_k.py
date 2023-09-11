from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int,
    ) -> Optional[ListNode]:
        if head is None:
            return None
        head_new, tail_node, remaining = self.helper(head, k)
        while remaining is not None:
            tail_prev, tail_next, remaining = self.helper(remaining, k)
            if tail_node is None:
                break
            tail_node.next = tail_prev
            tail_node = tail_next
        return head_new

    def helper(
        self, head: ListNode, k: int
    ) -> Tuple[ListNode, Optional[ListNode], Optional[ListNode]]:
        if head.next is None:
            if k > 1:
                return head, None, None
            return head, head, None
        if k == 1:
            return head, head, head.next
        tail_reversed, tail_node, remaining = self.helper(head.next, k - 1)
        if tail_node is None:
            return head, None, remaining
        tail_node.next = head
        head.next = None
        return tail_reversed, head, remaining
