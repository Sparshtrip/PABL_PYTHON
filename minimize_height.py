class Solution:
    def getMinDiff(self, arr, k):
        
        if isinstance(arr, str):
            arr = list(map(int, arr.split()))
        
        n = len(arr)
        arr.sort()
        
        ans = arr[-1] - arr[0]
        
        small = arr[0] + k
        big = arr[-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            
            min_height = min(small, arr[i] - k)
            max_height = max(big, arr[i-1] + k)
            
            ans = min(ans, max_height - min_height)
        
        return ans
