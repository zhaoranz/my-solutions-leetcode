class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minv=-1 * pow(2,32)
        n3=n2=n1= minv
        
        if len(nums) ==1:
            return nums[0]
        if len(nums) ==2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        
        for num in nums:
            if num <=n3 or num ==n2 or num==n1:
                continue
            if num >n1:
                n3=n2
                n2=n1
                n1=num
            elif num > n2:
                n3=n2
                n2 = num
            else:
                n3=num
        return n1 if n3==minv else n3
