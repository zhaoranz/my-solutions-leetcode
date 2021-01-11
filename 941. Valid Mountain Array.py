class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i,j = 0, len(arr) -1
        while i < (len(arr) -1) and arr[i] <arr[i+1]:
            i +=1

        
        while j>0 and arr[j-1] >arr[j]:
            j -= 1
            
        return i >0 and j < len(arr) -1 and i == j
