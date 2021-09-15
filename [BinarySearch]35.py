class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1]<target:
            return len(nums)
        l, r=0, len(nums)
        while l<r:
            mid = l +((r-l)>>1)
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        return r
        
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
