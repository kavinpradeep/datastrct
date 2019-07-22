class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        gcd=self.findgcd(x,y)
        if gcd==0 and z==0:
            return True
        if gcd==0 and z>0:
            return False
        return 0 or ( x+y>=z and z%gcd==0 )
        
    def findgcd(self,x,y):
        if x==0:
            return y
        if y==0:
            return x
        return self.findgcd(y,x%y)