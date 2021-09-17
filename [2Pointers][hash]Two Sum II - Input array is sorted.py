class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d=dict()
        for i in range(len(numbers)):
            if target - numbers[i] not in d:
                d[numbers[i]]=i
            else:
                return d[target-numbers[i]]+1, i+1
              
              
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            total=numbers[l]+numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l +=1
            else:
                r-=1
        
