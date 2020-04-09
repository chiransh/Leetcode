class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp=[]
        dp.append(nums[0])
        max_sum=nums[0]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
            if dp[i]>max_sum:
                max_sum=dp[i]
        return max_sum