class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        
        def can_place(dist):
            count = 1
            last = arr[0]
            
            for i in range(1, n):
                if arr[i] - last >= dist:
                    count += 1
                    last = arr[i]
                if count >= k:
                    return True
            
            return False
        
        low = 0
        high = arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans