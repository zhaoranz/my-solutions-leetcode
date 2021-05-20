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
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res =[]
        def dfs(idx,r):
            if len(res) < idx:
                res.append([])
            res[idx-1].append(r.val)
            if r.left:
                dfs(idx+1, r.left)
            if r.right:
                dfs(idx+1, r.right)
        dfs(1,root)
        return res
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        di=defaultdict(list)
        def solve(root,level,di):
            if not root:return 
            di[level].append(root.val)
            if root.left:solve(root.left,level+1,di)
            if root.right:solve(root.right,level+1,di)
        solve(root,0,di)
        lis=list(di.keys())
        lis.sort()
        ans=[]
        for i in lis:
            ans.append(di[i])
        return ans
