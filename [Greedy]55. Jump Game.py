#greey
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums==[0]:
            return True
        n, rightmost=len(nums), 0
        for i in range(n):
            if i<=rightmost:
                rightmost=max(rightmost, i+nums[i])
                if rightmost >=n-1:
                    return True
        return False
