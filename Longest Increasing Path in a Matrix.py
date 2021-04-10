class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        directions =[(-1,0),(1,0),(0,-1),(0,1)]
        row, col = len(matrix), len(matrix[0])
        visited =[[0]*col for _ in range(row)]
        ans = 0
        
        def dfs(x,y):
            nonlocal ans
            compare =[]
            for dx,dy in directions:
                r, c = x+dx, y+dy
                if (0<=r<row) and (0<=c<col) and (matrix[r][c]>matrix[x][y]):
                    if visited[r][c]:
                        compare.append(visited[r][c])
                    else:
                        compare.append(dfs(r,c))
            visited[x][y] = max(compare)+1 if compare else 1
            ans = max(visited[x][y], ans)
            return visited[x][y]
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    dfs(i,j)
        return ans
