# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        def recur(root, cm):
            if root.val >= cm:
                self.res +=1
                cm = root.val
            if root.left:
                recur(root.left, cm)
            if root.right:
                recur(root.right, cm)
        recur(root,-int(1e9)+7)
        return self.res
