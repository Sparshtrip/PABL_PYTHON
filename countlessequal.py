class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        
        # Step 1: Find pivot (smallest element index)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        
        # Binary search helper to count elements <= x
        def count_in_range(l, r):
            ans = l - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= x:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        count = 0
        
        # Count in first sorted half
        if pivot < n:
            idx = count_in_range(pivot, n - 1)
            if idx >= pivot:
                count += idx - pivot + 1
        
        # Count in second sorted half
        if pivot > 0:
            idx = count_in_range(0, pivot - 1)
            if idx >= 0:
                count += idx + 1
        
        return count