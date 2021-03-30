class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        n = len(envelopes)
        res=[envelopes[0][1]]
        for i in range(1,n):
            h = envelopes[i][1]
            if h > res[-1]:
                res.append(h)
            else:
                idx = bisect.bisect_left(res,h)
                res[idx] = h
        return len(res)
        
