#User function Template for python3

class Solution:
    def increment(self, arr, N):
        for i in range(len(arr)-1,-1,-1):
            if arr[i]!=9:
                arr[i]+=1
                return arr
            else:
                arr[i]=0
        return [1]+arr
                