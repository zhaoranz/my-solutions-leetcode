class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        dp=[[-prices[0],0,0]] + [[0]*3 for _ in range(n-1)]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1]=dp[i-1][0]+prices[i]
            dp[i][2]=max(dp[i-1][1], dp[i-1][2])
        return max(dp[n-1][1],dp[n-1][2])
      
#compact space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        dp0, dp1, dp2=-prices[0],0,0
        for i in range(1, n):
            new_dp0=max(dp0, dp2-prices[i])
            new_dp1=dp0+prices[i]
            new_dp2=max(dp2, dp1)
            dp0, dp1, dp2=new_dp0, new_dp1, new_dp2
        return max(dp1, dp2)
class Solution:
    def maxProfit(self, prices):
        hold, sold, cooldown = float("-inf"), 0, 0
        
        for price in prices:
            hold = max(hold, cooldown-price)
            cooldown = max(cooldown, sold)
            sold = max(sold, hold+price)
            
        return sold
              
