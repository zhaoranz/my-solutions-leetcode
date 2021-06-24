        def dfs(m,n,N,i,j):
            if (i<0 or j<0 or i >=m or j >=n):
                return 1
            if N==0:
                return 0
            dirs =[[-1,0],[1,0],[0,-1],[0,1]]
            res=0
            for d in dirs:
                new_i, new_j = i+ d[0],j+d[1]
                res += dfs(m,n,N-1,new_i, new_j)
            return res
        return dfs(m,n,maxMove,startRow,startColumn)
##m2
from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(i, j, u):
            #if u <= 0 or i < 0 or i >= m or j < 0 or j >= n:
            if (i < 0 or i >= m or j < 0 or j >= n):
                return 1
            elif u <=0:
                return 0
            return dfs(i-1, j, u-1) + dfs(i+1, j, u-1) + dfs(i, j-1, u-1) + dfs(i, j+1, u-1)
        
        return dfs(startRow, startColumn, maxMove) % (10**9+7)
class Solution:
    def findPaths(self, R: int, C: int, N: int, sr: int, sc: int) -> int:
        MOD = 10**9 + 7
        nxt = [[0] * C for _ in range(R)]
        nxt[sr][sc] = 1

        ans = 0
        for time in range(N):
            cur = nxt
            nxt = [[0] * C for _ in range(R)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < R and 0 <= nc < C:
                            nxt[nr][nc] += val
                        else:
                            ans += val

        return ans % MOD
        
