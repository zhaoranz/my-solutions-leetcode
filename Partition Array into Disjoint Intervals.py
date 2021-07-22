class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        nums_max = nums[0]
        allMax = nums[0]
        solution = 1
        for i in range(1, len(nums)):
            if nums[i] < nums_max:
                solution = i + 1
                nums_max = allMax
            else:
                allMax = max(allMax, nums[i])
        return solution
      
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        maxleft, minright=[None]*n, [None]*n
        
        tmp=nums[0]
        
        for i in range(n):
            tmp=max(tmp, nums[i])
            maxleft[i]=tmp
        tmp=nums[n-1]
        for i in range(n-1,-1,-1):
            tmp=min(tmp, nums[i])
            minright[i]=tmp
        for i in range(1,n):
            if maxleft[i-1] <= minright[i]:
                return i
