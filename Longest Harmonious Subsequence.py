class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l = r = ans = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                ans = max(ans, r - l + 1)
                
        return ans
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic1 = {}
        ans = 0
        for num in nums:
            dic1[num] = dic1.get(num,0) + 1
        for key in dic1:
            if (key + 1) in dic1:
                ans = max(ans, dic1[key] + dic1[key+1])

                
        return ans
                        
