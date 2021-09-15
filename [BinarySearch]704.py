class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r=0, len(nums)
        while l < r:
            mid = l +((r-l)>>1)
            if nums[mid]==target:
                return mid
            
                
            elif nums[mid]>target:
                r=mid
            else:
                l=mid+1
            
        return -1
        
