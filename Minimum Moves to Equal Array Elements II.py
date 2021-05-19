class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        total = 0
        nums.sort()
        while l<r:
            total += nums[r] - nums[l]
            r -=1
            l +=1
            
        return total
