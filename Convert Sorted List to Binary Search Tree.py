# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_len(head:ListNode) -> int:
            res = 0
            while head:
                res+=1
                head= head.next
            return res
        def build_tree(left:int, right:int) -> TreeNode:
            if left > right:
                return 
            mid = (left+right+1)//2
            root=TreeNode()
            root.left = build_tree(left, mid-1)
            nonlocal head
            root.val=head.val
            head=head.next
            root.right = build_tree(mid+1, right)
            return root
        l=get_len(head)
        return build_tree(0, l-1)
