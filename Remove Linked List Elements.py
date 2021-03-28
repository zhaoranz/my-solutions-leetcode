# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, None)
        dummy.next = head
        pred = dummy
        curr = head
        while curr:
            if curr.val == val:
                pred.next = curr.next
            else:
                pred = curr
            curr = curr.next
        return dummy.next
