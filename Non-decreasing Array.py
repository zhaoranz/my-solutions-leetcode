class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n=len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count +=1
                if  i >0 and i < n-2 and  nums[i-1] > nums[i+1] and nums[i]>nums[i+2]:
                    return False
    
        return count <2
        
