# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d ==1:
            return TreeNode(v, root)
        q = deque([root])
        while q:
            d -=1
            l = len(q)
            for _ in range(l):
                temp= q.popleft()
                if d==1:
                    temp.left = TreeNode(v, left =temp.left)
                    temp.right =TreeNode(v, right=temp.right)
                else:
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
        return root
#solution 2:recursion:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return
        if d==1:
            return TreeNode(v, root)
        if d==2:
            L = TreeNode(v, left = root.left)
            R = TreeNode(v, right = root.right)
            root.left =L
            root.right =R
            return root
        self.addOneRow(root.left, v, d-1)
        self.addOneRow(root.right,v, d-1)
        return root
