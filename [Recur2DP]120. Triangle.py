#time limited:
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dfs(triangle, i,j):
            if i==len(triangle):
                return 0
            return min(dfs(triangle,i+1,j),dfs(triangle,i+1,j+1))+triangle[i][j]
        
        return dfs(triangle, 0,0)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        memo=[[None]*n for _ in range(n)]
        
        def dfs(triangle, i,j):
            if i==len(triangle):
                return 0
            if memo[i][j]:
                return memo[i][j]
            memo[i][j]=min(dfs(triangle,i+1,j),dfs(triangle,i+1,j+1))+triangle[i][j]
            return memo[i][j]
        
        return dfs(triangle, 0,0)
#dp
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        f=[[0]*n for _ in range(n)]
        f[0][0]=triangle[0][0]
        for i in range(1, n):
            f[i][0]=f[i-1][0]+triangle[i][0]
            for j in range(1, i):
                f[i][j]=min(f[i-1][j-1],f[i-1][j])+triangle[i][j]
            f[i][i]=f[i-1][i-1]+triangle[i][i]
        return min(f[n-1])
    
 #compress space bottom --> top
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[0]*(n+1) for _  in range(n+1)]
        for i in range(n-1, -1,-1):
            for j in range(i+1):
                dp[i][j]=min(dp[i+1][j+1],dp[i+1][j])+triangle[i][j]
        return dp[0][0]
#compress 2
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp =[0]*(n+1)
        for i in range(n-1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
        
