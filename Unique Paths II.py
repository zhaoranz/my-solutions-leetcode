class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid),len(obstacleGrid[0])
        f=[0] * col
        f[0]=1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j]==1:
                    f[j] = 0
                    continue
                if j-1 >=0 and obstacleGrid[i][j-1]==0:
                    f[j] += f[j-1]
        return f[-1]
