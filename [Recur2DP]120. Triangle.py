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
    
    
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp =[0]*(n+1)
        for i in range(n-1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
        
