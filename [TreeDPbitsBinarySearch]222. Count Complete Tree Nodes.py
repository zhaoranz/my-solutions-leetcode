# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#tree+DP, general solution
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l=self.countNodes(root.left)
        r=self.countNodes(root.right)
        return l+r+1
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        level=0
        node=root.left
        while node:
            level+=1
            node=node.left
        l=1<<level
        r=(l<<1)-1
        while l<r:
            mid=int((r+l+1)/2)
            node=root
            bits=1<<(level-1)
            while node and bits>0:
                if mid&bits:
                    node=node.right
                else:
                    node=node.left
                bits >>=1
            if node:
                l=mid
            else:
                r=mid-1
        return r
