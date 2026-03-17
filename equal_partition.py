class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        
        target = total // 2
        
        if n % 2 == 0:
            sizes = [n // 2]
        else:
            sizes = [n // 2, n // 2 + 1]
        
        result = []
        
        def backtrack(index, chosen, curr_sum, size):
            if len(chosen) > size:
                return False
            
            if index == n:
                if len(chosen) == size and curr_sum == target:
                    result.append(chosen[:])
                    return True
                return False
            
            chosen.append(arr[index])
            if backtrack(index + 1, chosen, curr_sum + arr[index], size):
                return True
            chosen.pop()
            
            if backtrack(index + 1, chosen, curr_sum, size):
                return True
            
            return False
        
        for size in sizes:
            result.clear()
            if backtrack(0, [], 0, size):
                subset1 = result[0]
                subset2 = arr[:]
                for x in subset1:
                    subset2.remove(x)
                return [subset1, subset2]
        
        return []