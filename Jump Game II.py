class Solution:
    def jump(self, nums: List[int]) -> int:
        step, max_p, end =0,0,0
        for i in range(len(nums)-1):
            if max_p >=i:
                max_p = max(max_p, nums[i]+i)
                if i == end:
                    end = max_p
                    step +=1
        return step
            
