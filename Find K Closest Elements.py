class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n-k
        while left < right:
            mid = left +(right-left)//2
            if x - arr[mid] <= arr[mid+k] -x:
                right = mid
            else:
                left = mid + 1
        return arr[left: left+k]
