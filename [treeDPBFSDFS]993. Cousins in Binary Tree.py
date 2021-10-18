# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xParent, xDepth,xFound=None, None, False
        yParent, yDepth, yFound=None, None, False
        def dfs(node, parent, depth):
            if not node:
                return 
            nonlocal xParent, xDepth, xFound, yParent, yDepth, yFound
            if node.val==x:
                xParent, xDepth, xFound=parent, depth, True
            elif node.val==y:
                yParent, yDepth, yFound=parent, depth, True
            if xFound and yFound:
                return 
            dfs(node.left, node, depth+1)
            if xFound and yFound:
                return
            dfs(node.right, node, depth+1)
        dfs(root, None,0)
        return xParent!=yParent and xDepth==yDepth
#BFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xParent, xDepth, xFound=None, None, False
        yParent, yDepth, yFound=None, None, False
        def helper(node, parent, depth):
            nonlocal xParent, xDepth, xFound,yParent, yDepth, yFound
            if node.val==x:
                xParent, xDepth,xFound=parent, depth, True
            elif node.val==y:
                yParent, yDepth, yFound=parent, depth, True
        q=[(root,0)]
        helper(root, None, 0)
        while q:
            node, depth=q.pop(0)
            if node.left:
                q.append((node.left, depth+1))
                helper(node.left, node, depth+1)
            if node.right:
                q.append((node.right, depth+1))
                helper(node.right, node, depth+1)
            if xFound and yFound:
                break
        return xDepth==yDepth and xParent!=yParent
