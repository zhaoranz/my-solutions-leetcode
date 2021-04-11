# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q= [root]
        while True:
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            if new_q:
                q = new_q
            else:
                return sum(map(lambda x:x.val, q))
# Solution 2     

class Solution:
    def __init__(self):
        self.maxdepth = -1
        self.total = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def dfs(node, depth):
            if not node:
                return
            if depth > self.maxdepth:
                self.maxdepth, self.total = depth, node.val
            elif depth == self.maxdepth:
                self.total += node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root,0)
        return self.total
        
