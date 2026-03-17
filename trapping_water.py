
class Solution:
    def maxWater(self, arr):
        n=len(arr)
        l=0
        r=n-1
        lmax,rmax,res=0,0,0
        while l<r:
            if(arr[l]<=arr[r]):
                if(arr[l]>=lmax):
                    lmax=arr[l]
                else:
                    res+=(lmax-arr[l])
                l+=1
            else:
                if(arr[r]>=rmax):
                    rmax=arr[r]
                else:
                    res+=(rmax-arr[r])
                r-=1
        return res