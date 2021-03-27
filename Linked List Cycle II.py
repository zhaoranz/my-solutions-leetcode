# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = fast = head
        while fast: 
            slow = slow.next
            if fast.next !=None:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                ptr = head
                while ptr !=slow:
                    ptr = ptr.next
                    slow= slow.next
                return ptr
        return None
