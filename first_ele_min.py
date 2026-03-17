class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        result = 0
        
        for i in range(n - 1, -1, -1):
            # Maintain increasing stack
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            # If stack is empty → extend till end
            if not stack:
                result += (n - i)
            else:
                result += (stack[-1] - i)
            
            stack.append(i)
        
        return result