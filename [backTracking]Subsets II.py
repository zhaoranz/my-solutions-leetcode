class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        path=[]
        def backtracking(nums,start):
            res.append(path[:])
            for i in range(start,n):
                if i > start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()
        backtracking(nums,0)
        
        return res
