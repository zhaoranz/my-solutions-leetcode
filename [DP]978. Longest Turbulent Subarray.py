class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        down, up=1,1
        res=1
        for i in range(1, len(arr)):
            if arr[i-1]> arr[i]:
                down=up+1
                up=1
            elif arr[i-1]<arr[i]:
                up=down+1
                down=1
            else:
                down, up=1,1
            res=max(res,down, up)
        return res
