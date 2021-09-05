class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k ==1:
            res=s
            for i in range(len(s)):
                res=min(res, s[i:]+s[:i])
            return res
        return ''.join(sorted(s))
