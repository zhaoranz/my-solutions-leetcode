class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        is_prime =[1]*n
        for i in range(2, n):
            if is_prime[i]:
                ans +=1
            for j in range(i*i, n, i):
                is_prime[j]=0
        return ans
        
