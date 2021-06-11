class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n=len(stones)
        total = [[0]*n for _ in range(n)]
        for l in range(n):
            for r in range(l, n):
                if l==r:
                    total[l][r]=stones[l]
                else:
                    total[l][r]=total[l][r-1] + stones[r]
        dp =[[0]*n for _ in range(n)]
        
        for l in range(n-1,-1,-1):
            for r in range(l+1,n):
                if l+1==r:
                    dp[l][r]=max(stones[l], stones[r])
                else:
                    del_l = total[l+1][r]-dp[l+1][r]
                    del_r = total[l][r-1] - dp[l][r-1]
                    dp[l][r]=max(del_l, del_r)
        return dp[0][n-1]
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        # DP[i][j] is the max difference in scores on the array stones[i .. j]
        
        n = len(stones)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            v = stones[i]
            run_sum = 0

            for j in range(i + 1, n):
                new_run = run_sum+stones[j]
                dp[j] = max(new_run - dp[j], run_sum+v - dp[j - 1])
                run_sum = new_run
        return dp[n - 1]
