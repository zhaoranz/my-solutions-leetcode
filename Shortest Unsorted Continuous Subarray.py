class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        min_v = nums[-1]
        max_v = nums[0]
        l, r = len(nums)-1, 0
        for i in range(len(nums)):
            if nums[i] >= max_v:
                #min_v = min(min_v, nums[i])
                max_v = nums[i]
            else:
                r = i
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= min_v:
                min_v = nums[i]
            else:
                l = i
                
        return r-l+1 if r-l+1 > 0 else 0
