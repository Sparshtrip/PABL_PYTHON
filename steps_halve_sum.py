import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2
        
        # max heap using negative values
        heap = [-x for x in arr]
        heapq.heapify(heap)
        
        current_sum = total
        operations = 0
        
        while current_sum > target:
            largest = -heapq.heappop(heap)
            half = largest / 2
            
            current_sum -= half
            heapq.heappush(heap, -half)
            
            operations += 1
        
        return operations