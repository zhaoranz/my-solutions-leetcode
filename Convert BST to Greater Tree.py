# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def Morris_succ(node:TreeNode) -> TreeNode:
       
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ
        
        count = 0
        node = root
        
        while node:
            if not node.right:
                count += node.val
                node.val = count
                node = node.left
            else:
                succ = Morris_succ(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    count += node.val
                    node.val = count
                    node = node.left
        return root
 
