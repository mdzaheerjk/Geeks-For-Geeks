class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        i=0
        j=1
        while j<=len(arr)-1:
            if arr[i]<=arr[j]:
                i+=1
                j+=1
                continue
            else:
                return False
        return True