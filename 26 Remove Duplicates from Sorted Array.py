# This is an easy task, since the array is sorted. so we can just make the pointers to move forward.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] !=nums[j]:
                i +=1
                nums[i]=nums[j]
            j += 1
        return i + 1  
