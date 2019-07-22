class Solution(object):
    
    def findCrossMax(self,leftsubarr,rightsubarr):
        leftmax=leftsubarr[-1]
        rightmax=rightsubarr[0]
        lsum=leftmax
        rsum=rightmax
        
        i=len(leftsubarr)-1
        j=0
        
        for x in range(len(leftsubarr)-2,-1,-1):
            lsum+=leftsubarr[x]
            if lsum>leftmax:
                leftmax=lsum
        
        for x in range(1,len(rightsubarr)):
            rsum+=rightsubarr[x]
            if rsum>rightmax:
                rightmax=rsum
                
        return rightmax+leftmax
            
        
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==1:
            return nums[0]
        
        leftmax=self.maxSubArray(nums[:len(nums)//2])
        rightmax=self.maxSubArray(nums[len(nums)//2:])
        crossmax=self.findCrossMax(nums[:len(nums)//2],nums[len(nums)//2:])
        
        return max(leftmax,rightmax,crossmax)