class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        result = []
        index_to_tree_list = {}
        return self.dfs(result, 1, n, index_to_tree_list)
        
    
    
    def dfs(self, result, start, end, index_to_tree_list):
        if start == end:
            return [TreeNode(start)]
        if start > end:
            return [None]
        if (start, end) in index_to_tree_list:
            return index_to_tree_list[(start, end)]
        
        root_trees = []
        for i in range(start, end + 1):
          
          ## 获得所有可行的左子树集合
            left_trees = self.dfs(result, start, i - 1, index_to_tree_list)
            #获得所有可行的右子树集合
            right_trees = self.dfs(result, i + 1, end, index_to_tree_list)
            #从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    root_trees.append(root)
                    
        index_to_tree_list[(start, end)] = root_trees

        return root_trees
            
        
