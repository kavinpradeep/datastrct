class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        chart=dict()
        maxlen=0
        for i in deck:
            if i in chart:
                chart[i]=chart[i]+1
            else:
                chart[i]=1
            if maxlen<chart[i]:
                maxlen=chart[i]
        curgcd=maxlen
        for i in deck:
            curgcd=self.gcd(curgcd,chart[i])
        if curgcd<2:
            return False
        return True
    
    def gcd(self,a,b):
        if a%b==0:
            return b
        if b%a==0:
            return a
        return self.gcd(b,a%b)