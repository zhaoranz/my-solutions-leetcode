class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        def find_first(nums, target):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l+(r-l)//2
                if nums[mid] >= target:
                    r = mid -1 
                else:
                    l = mid +1
            return l
        first = find_first(nums, target)
        end = find_first(nums, target+1) -1
        
        return [first, end]
        
