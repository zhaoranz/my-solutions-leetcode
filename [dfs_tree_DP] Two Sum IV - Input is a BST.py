# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res=set()
        def dfs(root):
            nonlocal res
            if not root:
                return False
            if k - root.val in res:
                return True
            res.add(root.val)
            return dfs(root.left) or dfs(root.right)
        return dfs(root)
        
