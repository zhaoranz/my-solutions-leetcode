class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(a,low, high):
            pivot = a[low]
            i, j = low, high
            while i < j:
                while a[j] > pivot and i < j :
                    j-=1
                if i < j:
                    a[i] = a[j]
                    i +=1
                while a[i] < pivot and i < j:
                    i +=1
                if i < j :
                    a[j] = a[i]
                    j -= 1
            a[i]= pivot
            return i
        def quicksort(a, low, high):
            if low > high:
                return
            idx = partition(a, low, high)
            quicksort(a, low, idx-1)
            quicksort(a, idx+1, high)
        quicksort(nums, 0, len(nums)-1)
        return nums
