#dp
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon), len(dungeon[0])
        if not dungeon or m==0 or n==0:
            return 1
        dp=[[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1, -1,-1):
                if i==m-1 and j==n-1:
                    dp[i][j]=max(1, 1-dungeon[i][j])
                elif i==m-1:
                    dp[i][j]=max(1, dp[i][j+1]-dungeon[i][j])
                elif j==n-1:
                    dp[i][j]=max(1, dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j]=max(1, min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])
        

        return dp[0][0]
#dp2
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]
