class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s), len(t)
        if m < n:
            return 0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][n]=1
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j]=dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j]
        return dp[0][0]
        
from functools import lru_cache

global s
global t


@lru_cache(None)
def get_distinct_subsequence(i, j):
    """
    i -> s : larger
    j -> t : smaller
    """
    if j < 0:
        return 1

    if i < 0:
        return 0

    if s[i] == t[j]:
        return get_distinct_subsequence(i-1, j) + get_distinct_subsequence(i-1, j-1)
    
    return get_distinct_subsequence(i-1, j)
    
    

class Solution:
    def numDistinct(self, _s: str, _t: str) -> int:
        global s, t
        
        s = _s
        t = _t
        
        l1 = len(s)
        l2 = len(t)
        
        if l1 <= l2 and s != t:
            return 0
        
        if s == t:
            return 1
        
        get_distinct_subsequence.cache_clear()
        return get_distinct_subsequence(l1-1, l2-1)
