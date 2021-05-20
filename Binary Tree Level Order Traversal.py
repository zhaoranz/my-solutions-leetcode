# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue =[root]
        while queue:
            cur_size = len(queue)
            tmp =[]
            
            for _ in range(cur_size):
                cur_root = queue.pop(0)
                tmp.append(cur_root.val)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
            res.append(tmp)
        return res
        
