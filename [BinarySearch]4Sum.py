

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, nums, n = set(), sorted(nums), len(nums)
        numDict = {num: i for i, num in enumerate(nums)}
        numNext = [numDict[nums[i]] + 1 for i in range(n)]
        i = bisect_left(nums, target - nums[n-1] * 3, 0, n)
        right1 = bisect_right(nums, target / 4, i, n)
        while i < right1:
            end2 = bisect_right(nums, target - nums[i] * 3, i + 1, n)
            target2 = target - nums[i]
            j = bisect_left(nums, target2 - nums[end2-1] * 2, i + 1, end2)
            right2 = bisect_right(nums, target2 / 3, j, end2)
            while j < right2:
                end3 = bisect_right(nums, target2 - nums[j] * 2, j + 1, n)
                target3 = target2 - nums[j]
                k = bisect_left(nums, target3 - nums[end3-1], j + 1, end3)
                right3 = bisect_right(nums, target3 / 2, k, end3)
                while k < right3:
                    target4 = target3 - nums[k]
                    if (target4 in numDict) and (numDict[target4] > k):
                        res.add((nums[i], nums[j], nums[k], target4))
                    k = numNext[k]
                j = numNext[j]
            i = numNext[i]
        return res

