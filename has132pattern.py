class Solution:
    def has132Pattern(self, arr):
        stack = []
        third = float('-inf')
        
        for num in reversed(arr):
            if num < third:
                return True
            
            while stack and stack[-1] < num:
                third = stack.pop()
            
            stack.append(num)
        
        return False