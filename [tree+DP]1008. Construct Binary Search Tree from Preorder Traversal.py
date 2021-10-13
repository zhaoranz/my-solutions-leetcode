# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        if n==0:
            return 
        
        def dfs(preorder, left, right):
            if left>right:
                return
            root=TreeNode(preorder[left])
            if left==right:
                return root
            l,r=left, right
            while l<r:
                mid=l+(r-l+1)//2
                if preorder[mid]<preorder[left]:
                    l=mid
                else:
                    r=mid-1
            leftTree=dfs(preorder, left+1, l)
            rightTree=dfs(preorder, l+1, right)
            root.left=leftTree
            root.right=rightTree
            return root
        return dfs(preorder, 0, n-1)
      
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            root=TreeNode(preorder[0])
            devide=next((i for i, val in enumerate(preorder) if val>root.val),len(preorder))
            root.left=self.bstFromPreorder(preorder[1:devide])
            root.right=self.bstFromPreorder(preorder[devide:])
            return root
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            p, root = [[], []], TreeNode(preorder.pop(0))
            [p[val > root.val].append(val) for val in preorder]
            root.left = self.bstFromPreorder(p[0])
            root.right = self.bstFromPreorder(p[1])
            return root
