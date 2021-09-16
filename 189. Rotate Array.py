class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        n = len(A)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        n=len(nums)
        start=0
        while n and k:
          k%=n
          for i in range(0, k):
              nums[i+start],nums[n-k+i+start]=nums[n-k+i+start],nums[i+start]
          n-=k
          start+=k
            
