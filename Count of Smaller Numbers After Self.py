class BinaryIndexedTree:
    def __init__(self, length):
        self.c = [0]*length
    def lowBit(self,x):
        return x & (-x)
    def update(self, pos, value = 1):
        while pos < len(self.c):
            self.c[pos] += value
            pos += self.lowBit(pos)
    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.c[pos]
            pos -= self.lowBit(pos)
        return ans
class Solution:
    def discretization(self, nums):
        a = sorted(set(nums))
        value2ID ={v: i+1 for i, v in enumerate(a)}
        return value2ID, len(a)
    def countSmaller(self, nums: List[int]) -> List[int]:
        value2ID, length = self.discretization(nums)
        BIT = BinaryIndexedTree(length +1)
        ans = []
        
        for i  in reversed(range(len(nums))):
            posID= value2ID[nums[i]]
            ans.append(BIT.query(posID-1))
            BIT.update(posID)
            
        return ans[::-1]
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lst = deque()
        
        for item in range(len(nums) - 1, -1, -1):
            val = nums[item]
            if not lst or val > lst[len(lst) - 1]:
                nums[item] = 0 if not lst else len(lst)
                lst.append(val)
            else:
                i, j = 0, len(lst) - 1
                while i <= j:
                    mid = i + (j - i) // 2

                    if lst[mid] < val:
                        i = mid + 1
                    if lst[mid] >= val:
                        j = mid - 1
        
                nums[item] = i
                lst.insert(i, val)
        
        return nums
        
            
