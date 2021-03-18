class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        pre_diff = nums[1] - nums[0]
        count =2 if pre_diff !=0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]Wiggle Subsequence
            if (diff<0 and pre_diff>=0) or (diff >0 and pre_diff <=0):
                count += 1
                pre_diff = diff
        return count
