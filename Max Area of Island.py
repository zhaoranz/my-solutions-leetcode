#BFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        m,n=len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=1:
                    continue
                cnt=0
                q=[(i,j)]
                grid[i][j]*=-1
                while q:
                    x,y=q.pop(0)
                    cnt+=1
                    res=max(res, cnt)
                    for direct in dirs:
                        X,Y=x+direct[0],y+direct[1]
                        if 0<=X<m and 0<=Y<n and grid[X][Y]>0:
                            grid[X][Y] *=-1
                            q.append((X,Y))
        return res
                
                        
#DFS
class Solution:
    def dfs(self, grid, cur_i, cur_j) -> int:
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] !=1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            n_i, n_j = cur_i+di, cur_j+dj
            ans += self.dfs(grid, n_i, n_j)
        return ans
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i,j), ans)
        return ans
        
