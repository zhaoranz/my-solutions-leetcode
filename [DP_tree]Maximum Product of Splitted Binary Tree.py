# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        

        sub_sums = []

        def check_next(node: TreeNode):
            if node.left:
                check_next(node.left)
                node.val += node.left.val
            if node.right:
                check_next(node.right)
                node.val += node.right.val
            sub_sums.append(node.val)

        check_next(root)
        sub_sums.sort()
        tree_sum = sub_sums[-1]
        idx = bisect_left(sub_sums, tree_sum / 2)
        return (max((tree_sum - sub_sums[idx]) * sub_sums[idx],
                    (tree_sum - sub_sums[idx - 1]) * sub_sums[idx - 1])
                % 1_000_000_007)
      
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod=10**9+7
        def get_sum(root):
            if not root:
                return 
            nonlocal total
            total += root.val
            get_sum(root.left)
            get_sum(root.right)
        total=0
        get_sum(root)
        
        res=float('-inf')
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            sub_sum= root.val + left + right
            nonlocal res
            res = max(res, sub_sum * (total -sub_sum))
            return sub_sum
        dfs(root)
        return res%mod
            
