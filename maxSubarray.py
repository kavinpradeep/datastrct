class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==0:
            return 0
        
        sums=[nums[0]]
        for x in range(1,len(nums)):
            if(nums[x]>sums[x-1]+nums[x]):
                sums.append(nums[x])
            else:
                sums.append(nums[x]+sums[x-1])
        
        return max(sums)