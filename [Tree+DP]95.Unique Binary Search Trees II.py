# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res=[]
        index_to_tree_list={}
        return self.dfs(res, 1,n,index_to_tree_list)
    def dfs(self, res, start, end, index_to_tree_list):
        if start==end:
            return[TreeNode(start)]
        if start > end:
            return [None]
        if (start, end) in index_to_tree_list:
            return index_to_tree_list[(start,end)]
        root_trees=[]
        for i in range(start, end+1):
            left_trees=self.dfs(res, start, i-1, index_to_tree_list)
            right_trees=self.dfs(res, i+1, end, index_to_tree_list)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root=TreeNode(i)
                    root.left=left_tree
                    root.right=right_tree
                    root_trees.append(root)
        index_to_tree_list[(start, end)]=root_trees
        
        return root_trees
        
