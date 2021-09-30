class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total,n=sum(nums),len(nums)
        used=set()
        nums.sort()
        #//剪枝1求出数组总和sum，如果sum除以k不为整数，肯定就不满足每个组的和相等,直接return false.



        if total%k !=0:
            return False
    #拿到sum/k的值target后，target就代表每个组的和需要达到的值(超过或不足都不行)
        target=total/k
      #同时，如果数组的最大值>target也无法满足题意，return false.
        if nums[n-1]> target:
            return False
        def dfs(nums, begin, target, curSum, k, used):
            if k==1:
                return True #当我们在数组中找到k-1个满足题意的组合后，就可以return true了。因为剩下未选的元素的和肯定为数组总和sum-(k-1)*target=target。

            if curSum==target:
                return dfs(nums, n-1, target, 0, k-1, used) #//找到了一个组合,还有k-1个.
            for i in range(begin,-1,-1): #start from the largest elements
                if i in used: #index in used set will not be considered any more
                    continue
                if curSum + nums[i]>target:#排序后，从大到小枚举，先枚举的超过目标值, continue
                    continue
                used.add(i)#register this index to used
                if(dfs(nums, i-1, target, curSum+nums[i], k, used)):
                    return True#如果添加这个元素后，完成了题目要求, return true
                used.remove(i) #back track, remove this index from used set.
                while(i>0 and nums[i-1]==nums[i]):
                    i -=1 #dinstinct, if ith element cannot satisfy, then other elements with the same value cannot satisfy either
            return False
        return dfs(nums, n-1, target, 0, k, used)
      
      #DP:slower than the backtracking.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        basket, rem=divmod(sum(nums), k)
        nums.sort(reverse=True)
        if rem or nums[0]>basket:
            return False
        dp=[-1]*(1<<n)
        dp[0]=0
        for mask in range(1<<n):
            for j in range(n):
                nabo=dp[mask^(1<<j)]
                if mask & (1<<j) and nabo>=0 and nabo+nums[j]<=basket:
                    dp[mask]=(nabo+nums[j])%basket
                    break
                    
        return dp[-1] == 0
