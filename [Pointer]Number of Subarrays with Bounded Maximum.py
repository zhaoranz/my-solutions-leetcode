class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        temp = 0
        j = -1
        for i in range(len(nums)):
            if nums[i] > right:
                j = i
            if nums[i] >= left:
                temp = i - j
            ans += temp
        return ans
        
