class Solution:
    def countDigits(self, n):
        if n==0:
            return 1
    #  code here 
        count=0
        while n>0:
            n=n//10
            count+=1
        return count