class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastnonzero=0
        cur=0
        while cur<len(nums):
            if nums[cur]==0:
                pass
            else:
                nums[lastnonzero]=nums[cur]
                if lastnonzero != cur:
                    nums[cur]=0
                lastnonzero+=1
            cur+=1
        return nums
            
        