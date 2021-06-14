class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        for num, size in boxTypes:
            count = min(truckSize, num)
            res+=count*size
            truckSize -= count
            if truckSize ==0:
                break
        return res
