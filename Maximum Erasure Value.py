class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        window = set()
        total = 0
        l = 0
        ans=0
        for r in range(n):
            while window and nums[r] in window:
                window.remove(nums[l])
                total -= nums[l]
                l += 1
            window.add(nums[r])
            total += nums[r]
            ans = max(ans, total)
        return ans
        Maximum Erasure Value
