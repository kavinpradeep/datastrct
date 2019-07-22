class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        maxarea=0
        while start<end:
            breath=end-start
            length=min(height[start],height[end])
            area=breath*length
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
            if area>maxarea:
                maxarea=area
        return maxarea