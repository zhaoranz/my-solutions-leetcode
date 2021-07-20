class Solution:

    def __init__(self, nums: List[int]):
        self.array=nums
        self.origin=list(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array=self.origin
        self.origin=list(self.origin)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.array)):
            swap_idx=random.randrange(i,len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx],self.array[i]
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
