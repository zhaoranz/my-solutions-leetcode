class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m, n=len(grid), len(grid[0])
        res=0
        def dfs(grid, x, y, m, n):
            dirs=[(0,1),(0,-1),(1,0),(-1,0)]
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]==0:
                return 1
            if grid[x][y]==2:
                return 0
            grid[x][y]=2
            ans=0
            for d in dirs:
                nx,ny=x+d[0],y+d[1]
                ans += dfs(grid, nx,ny,m,n)
            return ans
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res +=dfs(grid,i,j, m,n)
        return res
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        for i in range(len(grid)):
            for j,val in enumerate(grid[i]):
                if val:
                    res +=4
                    if i>0 and grid[i-1][j]:
                        res -=2
                    if j>0 and grid[i][j-1]:
                        res -=2
        return res

