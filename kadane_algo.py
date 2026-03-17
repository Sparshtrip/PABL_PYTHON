class Solution:
    def maxSubArraySum(self, arr):
        res = arr[0]
        max_num=arr[0]
        n=len(arr)
        for i  in range(1,n):
            max_num=max(max_num +arr[i],arr[i])
            res=max(res,max_num)
        return res
        
