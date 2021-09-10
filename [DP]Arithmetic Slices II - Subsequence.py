        ans = 0
        f = [defaultdict(int) for _ in nums]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                cnt = f[j][d]
                ans += cnt
                f[i][d] += cnt + 1
        return ans
from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return 0
        
        dp = [defaultdict(int) for _ in range(size)]
        res = 0
        for i in range(size):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                if diff in dp[j]:
                    res += dp[j][diff]
        return res
