class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res,n=nums[0]+nums[1]+nums[2],len(nums)
       
        for i in range(n):
            if i!=0 and nums[i-1]==nums[i]:
               continue
            j,k=i+1,n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if abs(total-target) < abs(res-target):
                    res=total
                    
                if total < target:
                     j+=1
                
                    
                elif total > target:
                    k-=1
                   
                else:
                    return total
                    
                   
        return res
                    
