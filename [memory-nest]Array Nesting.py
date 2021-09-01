class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        visited=[0]*n
        for i in range(n):
            cur, count = i, 0
            while not visited[cur]:
                visited[cur]=1
                cur = nums[cur]
                count +=1
            res = max(res, count)
        return res
