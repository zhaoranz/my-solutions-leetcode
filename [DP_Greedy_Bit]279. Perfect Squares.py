#DP
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1, n+1):
            dp[i]=i
            j=1
            while(i-j*j)>=0:
                dp[i]=min(dp[i], dp[i-j*j]+1)
                j+=1
        return dp[n]
#Greedy
class Solution:
    def numSquares(self, n: int) -> int:
        ps=set([i*i for i in range(1, int(n**0.5)+1)])
        def divisible(n, count):
            if count==1: return n in ps
            for p in ps:
                if divisible(n-p, count-1):
                    return True
            return False
        for count in range(1, n+1):
            if divisible(n, count):
                return count
#Fastest
class Solution:
    def numSquares(self, n: int) -> int:
        def isSqrt(n):
            sqrtN=int(math.sqrt(n))
            return sqrtN*sqrtN==n
        if isSqrt(n):
            return 1
        while (n&3)==0:
            n>>=2
        if (n&7)==7:
            return 4
        for i in range(1, int(math.sqrt(n))+1):
            if isSqrt(n-i*i):
                return 2
        return 3
