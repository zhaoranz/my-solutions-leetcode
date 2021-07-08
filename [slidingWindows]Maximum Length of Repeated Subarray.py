class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def maxlen(addA:int,addB:int, l:int)->int:
            res, k = 0,0
            for i in range(l):
                if nums1[addA+i] == nums2[addB+i]:
                    k+=1
                    res = max(k, res)
                else:
                    k = 0
            return res
        res = 0
        n, m = len(nums1), len(nums2)
        
        for i in range(n):
            l = min(m, n-i)
            res = max(res, maxlen(i, 0, l))
        for i in range(m):
            l = min(n, m-i)
            res = max(res, maxlen(0, i, l))
        return res
        
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def check(length):
            seen = {A[i:i+length]
                    for i in range(len(A) - length + 1)}
            return any(B[j:j+length] in seen
                       for j in range(len(B) - length + 1))

        A = ''.join(map(chr, nums1))
        B = ''.join(map(chr, nums2))
        
        lo, hi = 0, min(len(A), len(B)) + 1
        
    
        while lo < hi:
            mi = hi - (hi - lo) // 2
            if check(mi):
                lo = mi
            else:
                hi = mi - 1
        return lo 
