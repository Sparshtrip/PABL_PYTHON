class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        left = [0] * n
        right = [0] * n
        
        stack = []
        
        # Count visible on left
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left[i] = i - stack[-1] - 1 if stack else i
            stack.append(i)
        
        stack.clear()
        
        # Count visible on right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            right[i] = stack[-1] - i - 1 if stack else n - 1 - i
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] + 1)
        
        return ans