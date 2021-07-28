class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo={1:[1]}
        def helper(n):
            if n not in memo:
                odds=helper((n+1)//2)
                evens=helper(n//2)
                memo[n]=[2*x-1 for x in odds]+[2*x for x in evens]
            return memo[n]
        return helper(n)
        
