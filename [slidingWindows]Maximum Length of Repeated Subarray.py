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
        
