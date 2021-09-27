class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res,freshLeft=0,0
        m, n=len(grid), len(grid[0])
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        
        q=[]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    freshLeft+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        while q and freshLeft >0:
            size=len(q)
            
            for i in range(size):
                x, y = q.pop(0)
                for d in dirs:
                    nx, ny=x+d[0],y+d[1]
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append((nx,ny))
                        freshLeft-=1
            res +=1
            
        
        
        return -1 if freshLeft>0 else res
