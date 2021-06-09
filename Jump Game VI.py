class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        max_sum_pointer = 0
        for i in range(1, n):
            if max_sum_pointer >= i - k:
                if max_sum < dp[i-1] and i > 0:
                    max_sum = dp[i-1]
                    max_sum_pointer = i - 1
            else:
                if i - k > 0:
                    max_sum = dp[i-k]
                    max_sum_pointer = i - k
                    for p in range(i-k, i):
                        if max_sum <= dp[p]:
                            max_sum = dp[p]
                            max_sum_pointer = p
                            
            dp[i] = max_sum + nums[i]
        
        dp[-1] = max_sum + nums[-1]
        return dp[-1]
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q=[(nums[0],0)]
        n = len(nums)
        res = nums[0]
        for i in range(1, n):
            while q and i - q[0][1] > k:
                q.pop(0)
            res = q[0][0] + nums[i]
            while q and q[-1][0] <= res:
                q.pop(-1)
            q.append((res,i))
        return res
        
