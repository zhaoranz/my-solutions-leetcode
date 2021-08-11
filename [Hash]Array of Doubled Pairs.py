class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d=Counter(arr)
        for n in sorted(d, key=abs):
            if d[n]==0:
                continue
            if (not n*2 in d) or (d[n*2] < d[n]):
                return False
            d[n*2] -= d[n]
            d[n]=0
        return True
        
