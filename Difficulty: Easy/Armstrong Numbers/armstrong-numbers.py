#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        digits=len(str(n))
        shallow_copy=n
        amstrong=0
        while n>0:
            last=n%10
            amstrong+=last**digits
            n//=10
        return amstrong==shallow_copy