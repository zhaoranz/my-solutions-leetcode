class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.total = sum(nums)
        

    def update(self, index: int, val: int) -> None:
        self.total -= self.nums[index]
        self.total += val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        
        if right - left > len(self.nums) // 2:
            return self.total - sum(self.nums[:left]) - sum(self.nums[right + 1:])
        else:
            return sum(self.nums[left: right + 1])
        
