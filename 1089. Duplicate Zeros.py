class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_len, count0 = len(arr), 0
        
        for i in range(len(arr)):
            if i > new_len -1 - count0:
                break
            if arr[i] ==0:
                if i == new_len - 1 - count0:
                    arr[new_len -1] =0
                    new_len -= 1
                    break       
                count0 +=1
                
        end = new_len - 1 - count0
            
        for j in range(end, -1, -1):
            if arr[j] ==0:
                arr[j + count0] = 0
                count0 -= 1
                arr[j + count0] = 0
            else:
                arr[j+count0] = arr[j]
                    
