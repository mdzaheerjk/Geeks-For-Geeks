import math
class Solution:
    def isPerfect(self, n):
        # code here 
        sum1=1
        if n==1:
            return False
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                sum1+=i
                if i!=n//i:
                    sum1+=n//i
        return sum1==n