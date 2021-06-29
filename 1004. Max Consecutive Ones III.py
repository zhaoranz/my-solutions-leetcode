class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        j = 0
        # always move right to expand sliding window, move left when k < 0
        for i in range(len(nums)):
            if nums[i] == 0: k -= 1
            if k < 0:
                if nums[j] == 0: k += 1
                j += 1
        return i - j + 1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        left, lsum, rsum = 0,0,0
        for right in range(n):
            rsum += 1 - nums[right]
            while lsum  < rsum - k:
                lsum += 1 - nums[left]
                left += 1
            res = max(res, right - left + 1)
        return res
