 class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans,n=0, len(nums)
        for i in range(n-1,1,-1):
            l,r=0, i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    ans+=r-l
                    r-=1
                else:
                    l+=1
        return ans
