#: Time Limit Exceeded !!
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n==2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
      
class Solution:
    @functools.lru_cache()#记忆化搜索」的注解
    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n==2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n==2:
            return 1
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=1
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
#most fast
class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=0,1,1
        for i in range(n):
            a,b,c=b,c,a+b+c
        return a
        
