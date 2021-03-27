class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        n=len(s)
        for i in range(n):
            for j in range(2):
                l=i
                r=i+j
                while l>=0 and r<n and s[l]==s[r]:
                    l-=1
                    r+=1
                    res+=1
        return res
        
