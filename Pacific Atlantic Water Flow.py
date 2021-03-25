class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    
        if not matrix or not matrix[0]: return []
        
        res1 = set()
        
        res2 = set()
        row = len(matrix)
        col = len(matrix[0])

        
        def dfs(i, j, res):
            res.add((i, j))
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[i][j] <= matrix[tmp_i][tmp_j] and (tmp_i, tmp_j) not in res: 
                    dfs(tmp_i, tmp_j, res)
       
        for i in range(row):
            dfs(i, 0, res1)
            dfs(i, col - 1, res2)
        
        for j in range(col):
            dfs(0, j, res1)
            dfs(row - 1, j, res2)
     
   
            
        return res1 & res2
