# Definition for singly-linked list.
from typing import List, Optional
from heapq import heappush, heappop
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            if len(lists) == 0:
                return ListNode("")
            elif len(lists[0]) == 1:
                return ListNode("")
        heap = []
        for list in lists:
            while list:
                heappush(heap, (list.val, list))
                list = list.next
        root = current = heappop(heap)[1]
        while heap:
            current.next = heappop(heap)[1]
            current = current.next

        return root


a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))
answer = Solution()
print(answer.mergeKLists([a, b, c]))

answer = Solution()
print(answer.mergeKLists([]))

answer = Solution()
print(answer.mergeKLists([[ListNode("")]]))
