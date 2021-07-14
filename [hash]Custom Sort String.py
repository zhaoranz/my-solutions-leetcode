class Solution:
    def customSortString(self, order: str, str: str) -> str:
        d = collections.Counter(str)
        res=[]
        for c in order:
            res.append(c*d[c])
            d[c]=0
        for c,v in d.items():
            res.append(c*v)
        return ''.join(res)Custom Sort String
