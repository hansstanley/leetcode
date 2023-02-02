from typing import List, Optional
from heapq import heapify, heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        curr: Optional[ListNode] = None
        lists_heap = [(l.val, i, l) for i, l in enumerate(lists) if l is not None]
        heapify(lists_heap)
        while len(lists_heap) > 0:
            v, i, l = heappop(lists_heap)
            if head is None: head = ListNode(v)
            if curr is None:
                curr = head
            else:
                curr_next = ListNode(v)
                curr.next = curr_next
                curr = curr_next
            if l.next is not None: heappush(lists_heap, (l.next.val, i, l.next))
        return head
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        curr: Optional[ListNode] = None
        lists = [l for l in lists if l is not None]
        while len(lists) > 0:
            lists.sort(key=lambda l: l.val)
            if head is None: head = ListNode(lists[0].val)
            if curr is None:
                curr = head
            else:
                curr_next = ListNode(lists[0].val)
                curr.next = curr_next
                curr = curr_next
            lists[0] = lists[0].next
            lists = lists[1:] if lists[0] is None else lists
        return head
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        non_empty = [l for l in lists if l is not None]
        if len(non_empty) == 0: return None
        non_empty.sort(key=lambda l: l.val)
        val_min = non_empty[0].val
        non_empty[0] = non_empty[0].next
        return ListNode(val_min, self.mergeKLists(non_empty))