class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[0],dp[1], dp[2]=0,1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
      
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        pre, cur=0,1
        for i in range(n):
            tmp=pre+cur
            pre, cur=cur, tmp
        return cur
      
      
import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        sqrt5=np.sqrt(5)
        alpha=(1+sqrt5)/2
        beta=(1-sqrt5)/2
        res=np.rint(((alpha**(n+1))-(beta**(n+1)))/sqrt5)
        return int(res)
    
            
