arr = [3, 5, 9, 12, 22, 54, 1, 69]

class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]

k = int(input("Enter the value of k: "))

obj = Solution()
result = obj.kthSmallest(arr, k)
print(f"{k}th smallest element is:", result)
