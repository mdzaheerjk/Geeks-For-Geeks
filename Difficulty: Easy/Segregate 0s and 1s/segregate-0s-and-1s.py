#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]==1 and arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            elif arr[i]==0:
                i+=1
            elif arr[j]==1:
                j-=1
        return arr
            
                